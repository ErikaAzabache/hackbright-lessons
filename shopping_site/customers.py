"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: %s, %s, %s>" % (
            self.fname, self.lname, self.email)


def get_customers():
    cust_file = open("customers.txt")
    customers_dict = {}

    for line in cust_file:
        cust_info = line.strip().split("|")
        fname = cust_info[0]
        lname = cust_info[1]
        email = cust_info[2]
        password = cust_info[3]
        customers_dict[email] = Customer(fname, lname, email, password)

    return customers_dict


def get_by_email(email):
    customers_dict = get_customers()

    return customers_dict[email]
