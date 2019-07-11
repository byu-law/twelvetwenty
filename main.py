from inc.twelvetwenty import TwelveTwenty
import inc.convert

choice = None
api = TwelveTwenty()

while choice is not 5:
    print("Subdomain: {}\t\tAuthenticated: {}\n".format(api.get_subdomain(), api.is_authenticated()))
    print("1. Enter 12Twenty subdomain")
    print("2. Authenticate the API")
    print("3. Import CSV of students")
    print("4. Get API documentation URL")
    print("5. Exit")

    try:
        choice = int(input("\nWhat is your choice? "))

        print("\n")

        if choice is 1:
            api.set_subdomain(input("Please enter the subdomain: "))
            print("\n")

        elif choice is 2:
            api.authenticate(input("Please enter the API key: "))
            print("\n")

        elif choice is 3:
            for row in inc.convert.csv_to_json(input("Enter the name of the CSV containing the student records: ")):
                try:
                    api.create_student(row)

                except Exception as e:
                    print(e)

            print("\n")

        elif choice is 4:
            print(api.get_documentation_url())
            print("\n")

    except Exception as e:
        print(e)
        print("\n")
