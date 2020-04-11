class GeoHash:
    """
    @param: latitude: one of a location coordinate pair 
    @param: longitude: one of a location coordinate pair 
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def __init__(self):
        self.d = {10:'b', 11:'c', 12:'d', 13:'e', 14:'f', 15:'g', 
             16:'h', 17:'j', 18:'k', 19:'m', 20:'n', 21:'p',
             22:'q', 23:'r', 24:'s', 25:'t', 26:'u', 27:'v', 
             28:'w', 29:'x', 30:'y', 31:'z'
        }
        self.geohash_bin_len = 30
        
    def encode(self, latitude, longitude, precision):
        # write your code here
        # a, b = latitude, longitude
        # if precision % 2 != 0:
        #     return 'error'
        # self.geohash_bin_len = math.ceil(precision/2)*5
        res_lat = self.foo(latitude, precision, -90, 90)
        res_lng = self.foo(longitude, precision, -180, 180)
        
        tmp = ''
        for i in range(len(res_lat)):
            tmp += res_lng[i]
            
            tmp += res_lat[i] # 先經後緯
            
        res = ''
        for j in range(0, len(tmp), 5):
            cur = self.bin2base32(tmp[j:j+5])
            res += cur
        return res[:precision]
        
    def bin2base32(self, s):
        res = 0
        for i in range(len(s)):
            res <<= 1
            res += (ord(s[i]) - ord('0'))
        return self.d[res] if res >= 10 else str(res)
        
    def foo(self, latitude, precision, lo, hi):
        i = 0
        res = ''
        while i < self.geohash_bin_len: #precision:
            mid = (lo+hi) / 2
            if latitude > mid:
                res += '1'
                lo = mid
            else:
                res += '0'
                hi = mid
            i += 1
        return res

sol = GeoHash()
print(sol.encode(39.92816697,
116.38954991,
12))
print(sol.encode(38.54,
-77.02,
10))
# 39.92816697
# 116.38954991
# 5


class GeoHash2:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        # write your code here
        base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        
        number = ''
        for i in range(len(geohash)):
            number += bin(base32.index(geohash[i]))[2:].zfill(5)        # padding to length 5
        
        lat = ''.join([number[i] for i in range(1, len(number), 2)])
        lng = ''.join([number[i] for i in range(0, len(number), 2)])
        
        
        # ans = "lat = {} and lng = {}".format(self.bin2real(lat, -90, 90), self.bin2real(lng, -180, 180))
        return [self.bin2real(lat, -90, 90), self.bin2real(lng, -180, 180)]
        
    def bin2real(self, s, lo, hi):
        
        for i in range(len(s)):
            mid = (lo + hi) / 2
            if s[i] == '1':
                lo = mid
            else:
                hi = mid
        
        return (lo+hi)/2
sol = GeoHash2()
print(sol.decode('w'))
print(sol.decode('wx4g0s'))
        