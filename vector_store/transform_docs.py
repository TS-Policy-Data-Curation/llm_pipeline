# TRANSFORMING THE DATA
def tableglom(doc):
    first_table = list(filter(lambda e: e.type=='table', doc.elements))[0]
    for elt in doc.elements:
        elt['path'] = doc.properties['path']
        if elt is first_table:
            continue
        elt.text_representation = f"Metadata: {first_table.table.to_csv()}\n{elt.text_representation}"

    return doc