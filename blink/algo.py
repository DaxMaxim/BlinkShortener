from blink.models import Links


class URL_Shortener:

    #give another parameter to the below function called 'id'


    def shorten_url(self, original_url, id):
        try:
            obj = Links.objects.filter(link = original_url)
            print(obj)
            print(type(obj))
            print(obj.values)
            print(type(obj.values))

        except Links.DoesNotExist:
            obj = None

        if obj:
            return obj[0].newlink
        else:
            shorten_url = self.encode(id)

        return "http://localhost:8000/"+shorten_url

    def encode(self, id):
        # base 62 characters
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        # convert base10 id into base62 id for having alphanumeric shorten url
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        # since ret has reversed order of base62 id, reverse ret before return it
        return "".join(ret[::-1])
