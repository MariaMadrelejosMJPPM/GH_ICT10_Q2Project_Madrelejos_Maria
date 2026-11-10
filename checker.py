from pyscript import document


def button(e):
    document.getElementById("results").innerHTML = '   '
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    members10 = {'Franchesca Dela Rosa', 'Destiny Reyes', 'Chalanie Lumbang', 'Vita De Guzman'}
    members9 = {'Gurleen Kaur', 'Julia Hadji Gapor', 'Raver Estacio'}
    members8 = {'Santiago Valdez', 'Jesse James Villante', 'Kenneth Concepcion'}
    members7 = {'Samantha Jose', 'Gisella Liwag', 'Hev Abi'}
    members = members10 | members9 | members8 | members7
    members.add(first + " " + last)
    
    document.getElementById("results").innerHTML = f"{members} Total Members: {len(members)}"