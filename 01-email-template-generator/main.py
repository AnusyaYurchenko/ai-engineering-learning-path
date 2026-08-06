def generate_email(template_file, output_file, customer_name, order_id):
    with open(template_file, "r", encoding="utf-8") as file:
        template = file.read()

    final_email = template.replace("CUSTOMER_NAME", customer_name)
    final_email = final_email.replace("ORDER_ID", order_id)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_email)

    return "File processing completed!"


def main():
    result = generate_email("email_template.txt", "email_to_send.txt", "Ana", "A1001")
    print(result)


if __name__ == "__main__":
    main()
