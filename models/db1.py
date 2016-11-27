db.define_table('image',
                Field('imagefile', 'upload'))

# user beid fields
db.define_table('cardreader',
    Field('cardnumber', 'string'),
    Field('chipnumber', 'string'),
    Field('validfrom', 'date'),
    Field('validtill', 'date'),
    Field('nationalnumber', 'string'),
    Field('name', 'string'),
    Field('firstnames', 'string'),
    Field('initials', 'string'),
    Field('nationality', 'string'),
    Field('birthlocation', 'string'),
    Field('birthdate', 'date'),
    Field('sex', 'string'),
    Field('noblecondition', 'string'),
    Field('doctumenttype', 'integer'),
    Field('specialstatus', 'integer'),
    Field('streetandnumber', 'string'),
    Field('zipcode', 'string'),
    Field('municipality', 'string'),
    Field('photo_id', 'reference image'))
