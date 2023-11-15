def bytes_to_megabytes(bytes_value):
    return bytes_value / (1024 ** 2)

def calculate_percentage(used_space, total_space):
    return (used_space / total_space) * 100

def generate_report(users):
    total_space = sum(users.values())
    average_space = total_space / len(users)

    with open('relatorio.txt', 'w') as f:
        f.write("ACME Inc. Uso do espaco em disco pelos usuarios\n")
        f.write("-" * 60 + "\n")
        f.write("{:<5} {:<15} {:<15} {:<10}\n".format("Nr.", "Usuario", "Espaco utilizado", "% do uso"))

        for i, (user, space) in enumerate(users.items(), start=1):
            space_mb = bytes_to_megabytes(space)
            percentage = calculate_percentage(space, total_space)
            f.write("{:<5} {:<15} {:<15.2f} MB {:<10.2f}%\n".format(i, user, space_mb, percentage))

        f.write("-" * 60 + "\n")
        f.write("Espaco total ocupado: {:.2f} MB\n".format(bytes_to_megabytes(total_space)))
        f.write("Espaco medio ocupado: {:.2f} MB\n".format(bytes_to_megabytes(average_space)))

def main():
    users = {}
    
    with open('usuarios.txt', 'r') as file:
        for line in file:
            user, space = line.strip().split()
            users[user] = int(space)

    generate_report(users)


main()