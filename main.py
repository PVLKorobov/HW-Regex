from DataThings import readCsv, cleanDataLists, getDict, mergeDuplicates, writeCsv
from pprint import pprint


if __name__ == '__main__':
    filename = 'phonebook_raw.csv'
    contacts = readCsv(filename)

    rowNames = contacts.pop(0)
    contacts = cleanDataLists(contacts)

    newContacts = []
    for contact in contacts:
        newContacts.append(getDict(contact))
    
    mergedData = mergeDuplicates(newContacts, rowNames)
    newContacts = mergedData[0]
    offset = 0
    for indexToDelete in mergedData[1]:
        del newContacts[indexToDelete - offset]
        offset += 1
    
    writeCsv(newContacts, rowNames)