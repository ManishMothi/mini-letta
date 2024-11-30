class RecallMemory:
    def __init__(self):
        self.memory = {}
    
    def add_entry(self, key: str, val: str):
        '''
        add key-value pair to recall memory. 
        '''
        self.memory[key] = val

    
    def fetch_memory(self) -> str:
        '''
        retrieve all recall memory as a formatted string
        '''
        return "\n".join(f"{key}: {value}" for key, value in self.memory.items())