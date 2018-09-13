def handle_error_by_throwing_exception():
  raise Exception("error")


def handle_error_by_returning_none(input_data):
  if input_data.isdigit():
    return int(input_data)


def handle_error_by_returning_tuple(input_data):
  if input_data.isdigit():
    return True, int(input_data)
  return False, None


def filelike_objects_are_closed_on_exception(filelike_object):
  with filelike_object as f:
    f.do_something()
