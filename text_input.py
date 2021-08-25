def text_input(prompt: str, choices: dict):
  player_input = input(prompt)
  while not player_input in choices.keys():
    print("""
    -------[Please choose a valid option]-------
    The valid options are displayed above this error
    """)
    player_input = input(prompt)
  res = choices[player_input]()
  return res