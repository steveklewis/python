import json
import leveldb


def main():
    db = leveldb.LevelDB('./db')
    TABLE_PREFIX_KEY = 'table_%s'
    value = {'hello': 'world1'}
    db.Put(TABLE_PREFIX_KEY % '1', json.dumps(value))
    value2 = {'hello': 'world2'}
    db.Put(TABLE_PREFIX_KEY % '2', json.dumps(value))

    for key, json_value in db.RangeIter(key_from='table_', key_to=None):
        print json_value
        value = json.loads(json_value)
        print value

if __name__ == '__main__':
     main()
