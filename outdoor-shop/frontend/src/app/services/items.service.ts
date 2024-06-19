import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, of, tap } from 'rxjs';
import { ItemDefinition, ItemStock } from './models';

@Injectable({
  providedIn: 'root',
})
export class ItemService {
  private backendUrl = 'http://localhost:8000';
  private cacheKey = 'productsCache';

  constructor(private http: HttpClient) {}

  getItemDefinitions(): Observable<ItemDefinition[]> {
    return this.http
      .get<ItemDefinition[]>(this.backendUrl + '/item-definitions')
      .pipe(
        tap((items) => this.cacheItemDefinitions(items)),
        catchError(
          this.handleError<ItemDefinition[]>(
            'get item definitions',
            this.getCachedItemDefinitions()
          )
        )
      );
  }

  getItemsStock(): Observable<ItemStock[]> {
    return this.http.get<ItemStock[]>(this.backendUrl + '/item-stock');
  }

  private cacheItemDefinitions(items: ItemDefinition[]): void {
    localStorage.setItem(this.cacheKey, JSON.stringify(items));
  }

  private getCachedItemDefinitions(): ItemDefinition[] {
    const cachedItems = localStorage.getItem(this.cacheKey);
    return cachedItems ? JSON.parse(cachedItems) : [];
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      return of(result as T);
    };
  }
}
