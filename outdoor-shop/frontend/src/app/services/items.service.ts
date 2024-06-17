import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { ItemDefinition, ItemStock } from './models';

const itemDefs: ItemDefinition[] = [
  { id: 'ID_1', name: 'Buty', color: 'Czarny' },
  { id: 'ID_2', name: 'Kurtka', color: 'Czarny' },
  { id: 'ID_3', name: 'Czapka', color: 'Czarny' },
  { id: 'ID_4', name: 'Szalik', color: 'Czarny' },
  { id: 'ID_5', name: 'Plecak', color: 'Czarny' },
  { id: 'ID_6', name: 'Bluza', color: 'Czarny' },
];

const itemsStock: ItemStock[] = [
  { id: 'ID_1', quantity: 12 },
  { id: 'ID_2', quantity: 1 },
  { id: 'ID_3', quantity: 4 },
  { id: 'ID_4', quantity: 90 },
  { id: 'ID_5', quantity: 14 },
  { id: 'ID_6', quantity: 0 },
];

@Injectable({
  providedIn: 'root',
})
export class ItemService {
  private backendUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getItemDefinitions(): Observable<ItemDefinition[]> {
    // return this.http.get<ItemDefinition>(this.backendUrl + '/items');
    return of(itemDefs);
  }

  getItemsStock(): Observable<ItemStock[]> {
    return of(itemsStock);
  }

  getItemQuantityLabel(quantity: number): string {
    if (quantity < 1) {
      return 'Brak';
    }
    if (quantity < 5) {
      return 'Ostatnie sztuki';
    }
    if (quantity < 15) {
      return 'Mała ilość';
    }
    return 'Na stanie';
  }
}
