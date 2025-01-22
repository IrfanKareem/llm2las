from pathlib import Path
import json
import hashlib

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

class SemanticParsingCache:
    def __init__(self, cache_file):
        self.dirty = False
        self.cache_file = cache_file
        if not Path(self.cache_file).exists():
            Path(self.cache_file).open('w').close()
        self.cache = self.load_cache()

    def load_cache(self):
        cache_dict = dict()
        for line in Path(self.cache_file).open('r').readlines():
            line_hash, response_json = line.split('|||')
            cache_dict[line_hash] = json.loads(response_json)
        return cache_dict

    def get_cache(self, line):
        h = hash_text(line.strip())
        if h in self.cache:
            return self.cache[h]
        return None
    
    def write_cache(self, line, value):
        h = hash_text(line.strip())
        if h in self.cache:
            raise RuntimeError("Value", line, "has already been cached. Unexpected")
        self.cache[h] = value
        self.dirty = True

    def __del__(self):
        if self.dirty:
            print(f"Cache {self.cache_file} has been updated. Writing to disk")
            self.dump_cache()

    def dump_cache(self):
        with open(self.cache_file, 'w') as f:
            for line_hash, response_json in self.cache.items():
                f.write(f"{line_hash}|||{json.dumps(response_json)}\n")
            f.flush()