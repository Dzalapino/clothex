import {
  HttpClient,
  HttpHeaders,
  HttpParams,
  HttpResponse,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable, of } from 'rxjs';
import { BasketItem, ImageDto, ItemDefinition2, ItemStock } from './models';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root',
})
export class ItemService {
  private backendUrl = 'http://localhost:8001';

  constructor(private http: HttpClient, private toastr: ToastrService) {}

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

  requestItems(item: BasketItem): Observable<string> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
    });

    return this.http.post<string>(
      this.backendUrl + '/request-items',
      {
        productId: item.productId,
        quantity: item.quantity,
      },
      { headers }
    );
  }

  getData(): Observable<Array<ItemDefinition2[]>> {
    return this.http
      .get<Array<ItemDefinition2[]>>(this.backendUrl + '/data', {
        observe: 'response',
      })
      .pipe(
        map((response: HttpResponse<Array<ItemDefinition2[]>>) => {
          if (response.status === 206) {
            this.toastr.warning('HQ not accessible. Displaying cached data!');
          }
          return response.body!;
        })
      );
  }

  getDataById(id: number): Observable<ItemDefinition2[]> {
    return this.http
      .get<ItemDefinition2[]>(this.backendUrl + '/data/' + id, {
        observe: 'response',
      })
      .pipe(
        map((response: HttpResponse<ItemDefinition2[]>) => {
          if (response.status === 206) {
            this.toastr.warning('HQ not accessible. Displaying cached data!');
          }
          return response.body!;
        })
      );
  }

  getImagesById(id: number): Observable<ImageDto[]> {
    return this.http
      .get<ImageDto[]>(this.backendUrl + '/images/' + id, {
        observe: 'response',
      })
      .pipe(
        map((response: HttpResponse<ImageDto[]>) => {
          if (response.status === 206) {
            this.toastr.warning('HQ not accessible. Displaying cached data!');
            console.log(response);
          }
          return response.body!;
        })
      );
  }
}
