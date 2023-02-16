from src.data_store import data_store

def clear_v1():
    store = data_store.get()
    store['users'] = []
    store['channels'] = []
    store['dms'] = []
    store['sendlaterIds'] = []
    store['workspace_stats'] = {
        'channels_exist': [], 
        'dms_exist': [], 
        'messages_exist': [], 
        'utilization_rate': 0
    }
    data_store.set(store)
