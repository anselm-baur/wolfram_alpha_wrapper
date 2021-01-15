import wolframalpha as wa
from numpy import sqrt


class WolframAlpha:
    def __init__(self, app_id):
        self.app_id = app_id
        self.client = wa.Client(self.app_id)
        self.result = None
        self.cmd = None
    
    
    def query(self,cmd):
        self.cmd = cmd
        print("query: "+cmd)
        self.result = self.client.query(cmd)

        return self._parse_result(self.result)


    def _parse_result(self,result):
        for r in result.pods:
            #print(f"found @title: {r['@title']}")
            if r["@title"] == "Solution":
                for sub in r.subpod:
                    res_str = sub.plaintext
                    res_str = res_str.replace("sqrt", "*sqrt")
                    res_value = eval(res_str.replace('x = ', ''))
                    print(res_str)
                    print(f"x = {res_value}")
                    return float(res_value)

            if r["@title"] == "Numerical solution":
                for sub in r.subpod:
                    res_str = sub.plaintext
                    res_str = res_str.replace("sqrt", "*sqrt")
                    res_value = eval((res_str.replace('x ≈ ', '')).replace("...",""))
                    print(res_str)
                    print(f"x = {res_value}")
                    return float(res_value)

    def get_last_result(self):
        return self._parse_result(self.result)
