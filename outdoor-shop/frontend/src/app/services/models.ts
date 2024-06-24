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

export interface ItemDefinition2 {
  product_id: number;
  product_name: string;
  product_item_id: number;
  product_code: string;
  retail_price: number;
  colour_name: string;
  size_option_name: string;
  variation_id: string;
}
