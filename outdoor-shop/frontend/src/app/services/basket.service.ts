import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BasketItem } from './models';

@Injectable({
  providedIn: 'root',
})
export class BasketService {
  private backendUrl = 'http://localhost:8001';
  private cacheKey = 'basketItems';
  private _basketItems: BasketItem[] | null = null;

  constructor(private http: HttpClient) {}

  getBasketItems(): BasketItem[] {
    if (!this._basketItems) {
      this._basketItems = JSON.parse(
        localStorage.getItem(this.cacheKey) ?? '[]'
      );
    }
    return this._basketItems ?? [];
  }

  addItemToBasket(item: BasketItem): BasketItem[] {
    const items = this.getBasketItems();

    const existingItemIndex = items.findIndex(
      (s) => s.productId === item.productId
    );
    if (existingItemIndex > -1) {
      items[existingItemIndex].quantity += item.quantity;
    } else {
      items.push(item);
    }
    this._basketItems = items;
    localStorage.setItem(this.cacheKey, JSON.stringify(this._basketItems));

    return this._basketItems;
  }

  removeItemFromBasket(id: number, quantity = 1): BasketItem[] {
    let items = this.getBasketItems();

    const existingItemIndex = items.findIndex((s) => s.productId === id);
    if (existingItemIndex > -1) {
      if (items[existingItemIndex].quantity <= quantity) {
        items.splice(existingItemIndex, 1);
      } else {
        items[existingItemIndex].quantity -= quantity;
      }
    }
    this._basketItems = items;
    localStorage.setItem(this.cacheKey, JSON.stringify(this._basketItems));
    if (this._basketItems.length === 0) {
      localStorage.removeItem(this.cacheKey);
    }

    return this._basketItems ?? [];
  }

  getBasketItemById(id: number): BasketItem | undefined {
    const items = this.getBasketItems();
    const itemIndex = items.findIndex((s) => s.productId == id);

    if (itemIndex > -1) {
      return items.at(itemIndex);
    } else {
      return undefined;
    }
  }
}
