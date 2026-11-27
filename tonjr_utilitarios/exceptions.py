class SaldoInsuficienteError(Exception):
    """Exceção levantada quando uma operação de saque excede o saldo disponível."""
    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para realizar o saque."):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        self.mensagem = (
            f'{mensagem} saldo atual de {saldo_atual:.2f} reais,'
            f'Tentativa de realizar o saque.{valor_saque:.2f} reais'
        )
        # Chama o construtor da classe Exception com a mensagem
        super().__init__(self.mensagem)

# Define a exceção para operações em contas inexistentes
class ContaInexistenteError(Exception):
    """Exceção levantada ao tentar operar numa conta que não existe."""
    def __init__(self, conta, mensagem="Conta inexistente."):
        self.conta = conta
        self.mensagem = f'{mensagem}, {conta}'
        super().__init__(self.mensagem)