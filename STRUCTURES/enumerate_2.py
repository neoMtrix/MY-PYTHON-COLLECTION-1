# Say you have a list of tuples containing two strings each. The first string is an email address and the second is the full name of the person with that email address. You want to write a function that creates a new list containing one string per person including their name and the email address between angled brackets. the format usually used in emails like this. So what do we need to do?

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))