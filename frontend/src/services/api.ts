const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getProducts() {
  const response = await fetch(`${API_URL}/api/v1/products/`);
  return response.json();
}

// Teste para conseguir conectar o backend aqui, tipo a api do backend