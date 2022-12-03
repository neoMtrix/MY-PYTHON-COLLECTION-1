# Imagine that your company has recently moved to using a new domain, but a lot of the company email addresses are still using the old one. You want to write a program that replaces this old domain with the new one in any outdated email addresses. The function to replace the domain would look like this.

def replace_domain(email, old_email, new_domain):
    if "@" + old_email in email:
        index = email.index("@" + old_email)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email