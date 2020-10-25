import datetime

class Pagamento:
    valor_pagamento = 0.0
    data_pagamento = ''
    def pagar(self):
        print(f"pagamento generico no valor {self.valor_pagamento} na data {self.data_pagamento}")

class PagamentoCartao(Pagamento):
    codigo_seguranca = 0
    def pagar(self):
        print(f"pagamento por cartao {self.valor_pagamento}")

p = Pagamento()
p.data_pagamento = datetime.date.today()
p.valor_pagamento = 4


x = Pagamento()
x.data_pagamento = "amanha"
x.valor_pagamento = 8

c = PagamentoCartao()
c.valor_pagamento = 1000
c.codigo_seguranca = 1
c.data_pagamento = ""

p.pagar()
x.pagar()
c.pagar()