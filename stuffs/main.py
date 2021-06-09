from replit import db

def handle_db(arguments):
  if arguments[0] == "key":
    if len(arguments) > 1:
      keys = db.keys()
      if arguments[1] in keys:
        return [0, db[arguments[1]]]
      else:
        return [0, "No key with name " + str(arguments[1])]
    else:
      return [1, "Too few argument"]
  elif arguments[0] == "list":
    keys = db.keys()
    if not bool(keys):
      keys = "No key"
    return [0, keys]
  elif arguments[0] == "set":
    if len(arguments) > 2:
      db[arguments[1]] = arguments[2]
      return [2, "Success"]
    else:
      return [1, "Too few argument"]
  elif arguments[0] == "help":
    return [2, "db list -> list all keys\ndb key $key -> get $key's value\ndb set $key $value -> set value $value to $key"]
  # elif arguments[0] == "clear":
  #   keys = db.keys()
  #   for i in keys:
  #     del db[i]
  #   return [2, "Success"]
  else:
    return [1, "No command"]