#dictionary={key:value}

item={
    "name":"Book",
    "item":5.67
}

print(item)

item={
    "name":"Book",
    "item":5.67
}

print(item["name"])


item={
    "name":"Book",
    "item":5.67
}
item["name"]="New Book"

print(item)


item={
    "name":"Book",
    "item":5.67
}
del(item["name"])

print(item)

item={
    "name":"Book",
    "price":5.67
}
item.pop("price")
print(item)


item={
    "name":"Book",
    "price":5.67
}
item["quantity"]=4
print(item)

item={
    "name":"Book",
    "price":5.67
}
item.update({"quantity":9})
print(item)

item={
    "name":"Book",
    "price":5.67
}
print(item.get("name"))

item={
    "name":"Book",
    "price":5.67
}
print(item.get("quantity",0))
