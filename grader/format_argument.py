def format_argument(message):
  command_name_size = message.find(' ')
  message = message[command_name_size + 1 : ]
  question_name_size = message.find(' ')
  question = message[ : question_name_size]
  message = message[ question_name_size + 1 : ]
  return question, message