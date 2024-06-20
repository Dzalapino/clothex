export interface ItemDefinition {
  id: number;
  name: string;
  color: string;
  imgUrl: string;
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
