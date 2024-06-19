export interface ItemDefinition {
  id: number;
  name: string;
  color: string;
}

export interface ItemStock {
  id: number;
  productId: number;
  quantity: number;
}

export interface BasketItem {
  productId: number;
  quantity: number;
}
