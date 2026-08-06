def generate_email(template_file, output_file, customer_name, order_id):
    with open(template_file, "r") as file:
        template = file.read()

    final_email = template.replace("CUSTOMER_NAME", customer_name)
    final_email = final_email.replace("ORDER_ID", order_id)

    with open(output_file, "w") as file:
        file.write(final_email)

    return "File processing completed!"


result = generate_email("email_template.txt", "email_to_send.txt", "Ana", "A1001")
print(result)
