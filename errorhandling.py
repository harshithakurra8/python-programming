contacts={
     "jerry":8687678,
     "ben":757765,
     "harry":66857867,
     "rao":8678767
}
client=input("Search🔍:")
try:
  print(client,contacts[client])
except KeyError:
    print(client,"Not found!")

   
contacts={
     "jerry":8687678,
     "ben":757765,
     "harry":66857867,
     "rao":8678767
}
class CapitalizationError(Exception):
    pass

client=input("Search🔍:")
if client[0]!=client[0].upper():
   raise CapitalizationError(
      client + "should be capitalized"
   )
try:
  print(client,contacts[client])
except KeyError:
    print(client,"Not found!")   


             