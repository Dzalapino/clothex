import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import {
  BasketItem,
  ItemDefinition,
  ItemDefinition2,
  ItemStock,
} from './models';

@Injectable({
  providedIn: 'root',
})
export class ItemService {
  private backendUrl = 'http://localhost:8001';

  constructor(private http: HttpClient) {}

  getItemDefinitions(): Observable<ItemDefinition[]> {
    return this.http.get<ItemDefinition[]>(
      this.backendUrl + '/item-definitions'
    );
  }

  getItemsStock(): Observable<ItemStock[]> {
    return this.http.get<ItemStock[]>(this.backendUrl + '/item-stock');
  }

  buyItems(item: BasketItem): Observable<string> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
    });

    return this.http.post<string>(this.backendUrl + '/buy-items', item, {
      headers,
    });
  }

  getItemById(id: number): Observable<ItemDefinition> {
    return this.http.get<ItemDefinition>(this.backendUrl + '/item/' + id);
  }

  requestItems(item: BasketItem): Observable<string> {
    return of('success');
  }

  getData(): Observable<Array<ItemDefinition2[]>> {
    return this.http.get<Array<ItemDefinition2[]>>(this.backendUrl + '/data');
  }

  getDataById(id: number): Observable<ItemDefinition2[]> {
    return this.http.get<ItemDefinition2[]>(this.backendUrl + '/data/' + id);
  }
}
