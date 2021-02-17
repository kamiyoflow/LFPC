from RegularGrammar import RegularGrammar


class FiniteAutomat:

    def __init__(self):
        self._states = []
        self._alphabet = []
        self._transitions = {}
        self._initialState = None
        self._finalStates = None

    @property
    def states(self):
        return self._states

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def transitions(self):
        return self._transitions

    @property
    def initial_state(self):
        return self._initialState

    @property
    def final_states(self):
        return self._finalStates


    @staticmethod
    def productionToDictionary(transitions):
        trans = {}
        for transition in transitions:
            transition_split = transition.split('->')
            final_trans = transition_split[1]
            initial_trans = transition_split[0].strip('(').strip(')').strip()
            lhs = initial_trans.split(',')
            trans[(lhs[0], lhs[1])] = final_trans
        return trans



    @states.setter
    def states(self, value):
        self._states = value

    @alphabet.setter
    def alphabet(self, value):
        self._alphabet = value

    @initial_state.setter
    def initial_state(self, value):
        self._initialState = value

    @final_states.setter
    def final_states(self, value):
        self._finalStates = value

    @transitions.setter
    def transitions(self, value):
        self._transitions = value

