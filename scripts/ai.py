from pydash import uniq_by
import csv

# Read from csv file


def readFromcsvFile():
    with open('../dataset/newData.csv', 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        next(reader)
        stringResult = ""

        for index, row in enumerate(reader):
            if not row.__contains__('@@'):
                row.append("@@")
            for index, column in enumerate(row):
                if index < len(row)-1:
                    stringResult += column + ","
                else:
                    stringResult += column
            stringResult += "\n"
    return stringResult


def unique_dataAndWriteToCSV():
    string_splitted = readFromcsvFile().split("@@")

    # String splitted removes the trailing white space
    # at the end of the list.
    string_splitted.pop()

    parse_to_list_of_objects = []

    for item in string_splitted:

        # Split each item in the array.
        splitted_item = item.split(",")

        # String splitted removes the trailing white space
        # at the end of the list of each item.
        splitted_item.pop()

        parse_to_list_of_objects.append(splitted_item)

    # Remove duplicates from the list of items.
    result = uniq_by(parse_to_list_of_objects, lambda item: item[0])

    # Specify the output CSV file path
    output_file = '../dataset/newDataCleaned.csv'

    # Open the file in write mode
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Name", "Current Inventory Level",	"Lead Time (in days)",	"Sales Velocity (in units per day)", "Highest Sales Month", "Supplier", "Unit Cost", "Reorder Point", "Safety Stock", "Festivals", "Supplier Lead Time (in days)", "Category", "Last Restock Date", "Next Restock Date"
                         ])
        writer.writerows(result)


# print(readFromcsvFile())
unique_dataAndWriteToCSV()
