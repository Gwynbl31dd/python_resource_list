# Define your function here
def package_enumerator(package):
    resources = dir(package)
    for resource in resources:
        print(resource)


if __name__ == '__main__':
    import string 
    package_enumerator(string)
