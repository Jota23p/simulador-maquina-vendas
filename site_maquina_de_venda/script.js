// --- CONTROLE DAS TELAS ---
const telas = document.querySelectorAll('.tela');
const menuButtons = document.querySelectorAll('#tela-menu .btn[data-target]');
const botoesVoltar = document.querySelectorAll('.btn-voltar');

// Função para mostrar uma tela específica e esconder as outras
function mostrarTela(idDaTela) {
    telas.forEach(tela => {
        if (tela.id === idDaTela) {
            tela.classList.remove('hidden');
        } else {
            tela.classList.add('hidden');
        }
    });
}

// Adiciona evento para os botões do menu principal
menuButtons.forEach(button => {
    button.addEventListener('click', () => {
        const targetTelaId = button.dataset.target;
        mostrarTela(targetTelaId);
    });
});

// Adiciona evento para TODOS os botões de "Voltar"
botoesVoltar.forEach(button => {
    button.addEventListener('click', () => {
        mostrarTela('tela-menu');
    });
});


// --- LÓGICA DO CADASTRO DE PRODUTOS ---
const formCadastro = document.getElementById('form-cadastro');
const nomeProdutoInput = document.getElementById('nome-produto');
const precoProdutoInput = document.getElementById('preco-produto');
const qtdProdutoInput = document.getElementById('qtd-produto');
const listaProdutosDiv = document.getElementById('lista-produtos');

// Nosso "banco de dados" de produtos em memória
const produtosCadastrados = [];

formCadastro.addEventListener('submit', (event) => {
    // Impede que o formulário recarregue a página
    event.preventDefault();

    // 1. Pega os valores dos inputs
    const nome = nomeProdutoInput.value;
    const preco = parseFloat(precoProdutoInput.value);
    const qtd = parseInt(qtdProdutoInput.value);

    // 2. Cria um objeto para o novo produto
    const novoProduto = {
        nome: nome,
        preco: preco,
        quantidade: qtd
    };

    // 3. Adiciona o novo produto ao nosso array
    produtosCadastrados.push(novoProduto);
    
    console.log('Produtos Cadastrados:', produtosCadastrados); // Para você ver no console do navegador
    
    // 4. Atualiza a lista de produtos na tela
    atualizarListaProdutos();

    // 5. Limpa os campos do formulário
    formCadastro.reset();
});

function atualizarListaProdutos() {
    // Limpa a lista atual
    listaProdutosDiv.innerHTML = '';

    if (produtosCadastrados.length === 0) {
        listaProdutosDiv.innerHTML = '<p>Nenhum produto cadastrado.</p>';
    } else {
        // Cria um elemento para cada produto e adiciona na div
        produtosCadastrados.forEach(produto => {
            const produtoElemento = document.createElement('p');
            produtoElemento.textContent = `${produto.nome} - R$ ${produto.preco.toFixed(2)} - Estoque: ${produto.quantidade}`;
            listaProdutosDiv.appendChild(produtoElemento);
        });
    }
}


// --- LÓGICA DA TELA DE PAGAMENTO ---
const opcoesPagamento = document.querySelectorAll('.opcao-pagamento');
let metodoSelecionado = null;

opcoesPagamento.forEach(opcao => {
    opcao.addEventListener('click', () => {
        // Remove a seleção de qualquer outra opção
        opcoesPagamento.forEach(op => op.classList.remove('selected'));
        // Adiciona a seleção na opção clicada
        opcao.classList.add('selected');
        metodoSelecionado = opcao.dataset.metodo;
        console.log("Método selecionado:", metodoSelecionado);
    });
});


// Inicializa a aplicação mostrando o menu principal
mostrarTela('tela-menu');