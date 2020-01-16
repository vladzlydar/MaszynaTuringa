# # # from tkinter import *
# # #
# # # root = Tk()
# # # def onClick():
# # #     binary = ciagEntry.get()
# # #     for child in tapeTM.winfo_children():
# # #         child.destroy()
# # #     tapeTM.grid_remove()
# # #     tapeTM.grid(row=1, column=0, columnspan=len(tapeTM.winfo_children())+1, sticky="we", pady=10)
# # #     for i in range(len(binary)):
# # #         if int(binary[i]) in [0,1]:
# # #             Label(tapeTM, text = binary[i], font= 25, fg = "black",  bg="white").grid(row = 1,  column =i ,sticky="we")
# # #             tapeTM.grid_columnconfigure(i, weight=1)
# # #             tapeTM.grid_rowconfigure(1, weight=1)
# # #             tapeTM.update()
# # #         else:
# # #             break
# # #
# # # tapeTM = Frame(root, height=40)
# # # aktualnyStanLabel = Label(root,  text= "AKTUALNY STAN MASZYNY:")
# # # aktualnyStanWskaznik = Label(root, width = 3, fg="red",  bg= "black" , font =16 )
# # # submitButton = Button(root, text ="Wprowadz ciag do maszyny", command = onClick)
# # # ciagEntry = Entry(root, width = 10)
# # #
# # #
# # # aktualnyStanLabel.grid(row = 0,column = 0)
# # # aktualnyStanWskaznik.grid(row = 0, column=1)
# # # tapeTM.grid(row=1, column=0, sticky="we", pady=10)
# # # ciagEntry.grid(row = 0,column = 3, padx=10)
# # # submitButton.grid(row=0, column = 4, sticky = E)
# # #
# # #
# # #
# # # root.mainloop()
# # #
# # #
# # #
# # #
# # class Tasma(object):
# #     symbol_pusty = "#"
# #
# #     def __init__(self,
# #                  tape_string=""):
# #         self.__tape = dict((enumerate(tape_string)))
# #         # last line is equivalent to the following three lines:
# #         # self.__tape = {}
# #         # for i in range(len(tape_string)):
# #         #    self.__tape[i] = input[i]
# #
# #     def __str__(self):
# #         s = ""
# #         min_used_index = min(self.__tape.keys())
# #         max_used_index = max(self.__tape.keys())
# #         for i in range(min_used_index, max_used_index):
# #             s += self.__tape[i]
# #         return s
# #
# #     def __getitem__(self, index):
# #         if index in self.__tape:
# #             return self.__tape[index]
# #         else:
# #             return Tasma.blank_symbol
# #
# #     def __setitem__(self, pos, char):
# #         self.__tape[pos] = char
# #
# # class TuringMachine(object):
# #
# #     def __init__(self,
# #                  tape="",
# #                  blank_symbol="#",
# #                  initial_state="",
# #                  final_states=None,
# #                  transition_function=None):
# #         self.__tape = Tasma(tape)
# #         self.__head_position = len(str(self.__tape))-1
# #         self.__blank_symbol = blank_symbol
# #         self.__current_state = initial_state
# #         if transition_function == None:
# #             self.__transition_function = {}
# #         else:
# #             self.__transition_function = transition_function
# #         if final_states == None:
# #             self.__final_states = set()
# #         else:
# #             self.__final_states = set(final_states)
# #
# #     def get_tape(self):
# #         return str(self.__tape)
# #
# #     def get_current_state(self):
# #         return  str(self.__current_state)
# #
# #     def step(self):
# #         char_under_head = self.__tape[self.__head_position]
# #         x = (self.__current_state, char_under_head)
# #         if x in self.__transition_function:
# #             y = self.__transition_function[x]
# #             self.__tape[self.__head_position] = y[1]
# #             if y[2] == "R":
# #                 self.__head_position += 1
# #             elif y[2] == "L":
# #                 self.__head_position -= 1
# #             self.__current_state = y[0]
# #
# #     def final(self):
# #         if self.__current_state in self.__final_states:
# #             return True
# #         else:
# #             return False
# #
# # initial_state = "q0",
# # accepting_states = ["qA"],
# # transition_function = {("q0","0"):("q1", "1", "L"),
# #                        ("q0","1"):("q2", "0", "L"),
# #                        ("q0","#"):("q0"," ", "L"),
# #                        ("q1", "0"): ("q3", "1", "L"),
# #                        ("q1", "1"): ("q4", "0", "L"),
# #                        ("q1", "#"): ("qA", "1", "L"),
# #                        ("q2", "0"): ("q5", "0", "L"),
# #                        ("q2", "1"): ("q6", "1", "L"),
# #                        ("q2", "#"): ("q4", "0", "L"),
# #                        ("q3", "0"): ("q3", "0", "L"),
# #                        ("q3", "1"): ("q3", "1", "L"),
# #                        ("q3", "#"): ("qA", " ", "L"),
# #                        ("q4", "0"): ("q3", "1", "L"),
# #                        ("q4", "1"): ("q4", "0", "L"),
# #                        ("q4", "#"): ("qA", "1", "L"),
# #                        ("q5", "0"): ("q3", "1", "L"),
# #                        ("q5", "1"): ("q5", "0", "L"),
# #                        ("q5", "#"): ("qA", "1", "L"),
# #                        ("q6", "0"): ("q3", "1", "L"),
# #                        ("q6", "1"): ("q6", "0", "L"),
# #                        ("q6", "#"): ("qA", "1", "L")
# #                        }
# # final_states = {"qA"}
# #
# # t = TuringMachine("#1101#",
# #                   initial_state = "q0",
# #                   final_states = final_states,
# #                   transition_function=transition_function)
# #
# # print("Input on Tape:\n" + t.get_tape())
# #
# # while not t.final():
# #     t.step()
# #     print(t.get_current_state())
# #
# # print("Result of the Turing machine calculation:")
# # print(t.get_tape())\
#
#
# tabelaPrzejsc = {
#     ("q0","0"):("q1", "1", "L"),
#     ("q0","1"):("q2", "0", "L"),
#     ("q0","#"):("q0"," ", "L"),
#     ("q1", "0"): ("q3", "1", "L"),
#     ("q1", "1"): ("q4", "0", "L"),
#     ("q1", "#"): ("qA", "1", "L"),
#     ("q2", "0"): ("q5", "0", "L"),
#     ("q2", "1"): ("q6", "1", "L"),
#     ("q2", "#"): ("q4", "0", "L"),
#     ("q3", "0"): ("q3", "0", "L"),
#     ("q3", "1"): ("q3", "1", "L"),
#     ("q3", "#"): ("qA", " ", "L"),
#     ("q4", "0"): ("q3", "1", "L"),
#     ("q4", "1"): ("q4", "0", "L"),
#     ("q4", "#"): ("qA", "1", "L"),
#     ("q5", "0"): ("q3", "1", "L"),
#     ("q5", "1"): ("q5", "0", "L"),
#     ("q5", "#"): ("qA", "1", "L"),
#     ("q6", "0"): ("q3", "1", "L"),
#     ("q6", "1"): ("q6", "0", "L"),
#     ("q6", "#"): ("qA", "1", "L")
# }
#
# stanPoczatkowy = "q0"
# stanyAkceptujace = ["qA"]
#
# dlugoscTasmy = 1000
#
# def maszynaTuringa(stanPoczatkowy,stanyAkceptujace,analizowanyCiag):
#
#     aktualnyStan = stanPoczatkowy
#     tasma = list(analizowanyCiag)
#     pozycjaGlowicy = len(analizowanyCiag)
#     while aktualnyStan not in stanyAkceptujace:
#
#
#

Code = {
     ("q0","0"):("q1", "1", "L"),
    ("q0","1"):("q2", "0", "L"),
    ("q0","#"):("q0","#", "L"),
    ("q1", "0"): ("q3", "1", "L"),
    ("q1", "1"): ("q4", "0", "L"),
    ("q1", "#"): ("qA", "1", "L"),
    ("q2", "0"): ("q5", "0", "L"),
    ("q2", "1"): ("q6", "1", "L"),
    ("q2", "#"): ("q4", "0", "L"),
    ("q3", "0"): ("q3", "0", "L"),
    ("q3", "1"): ("q3", "1", "L"),
    ("q3", "#"): ("qA", "#", "L"),
    ("q4", "0"): ("q3", "1", "L"),
    ("q4", "1"): ("q4", "0", "L"),
    ("q4", "#"): ("qA", "1", "L"),
    ("q5", "0"): ("q3", "1", "L"),
    ("q5", "1"): ("q5", "0", "L"),
    ("q5", "#"): ("qA", "1", "L"),
    ("q6", "0"): ("q3", "1", "L"),
    ("q6", "1"): ("q6", "0", "L"),
    ("q6", "#"): ("qA", "1", "L")
        }
string = input("Wprowadz ciag do analizy: ")

def simulate_tm(program,ciag):
    tape,  state = list(ciag), "q0"
    infBefore =["#"] *10
    infAfter = ["#"]* 10
    tape = infBefore +tape+ infAfter
    head = len(tape)-1
    print(state, tape)
    while not(state=="qA"):
        state, tape[head], d_head = program[state, tape[head]]
        head += 1 if d_head == "R" else -1
    return tape



print(simulate_tm(Code,string))