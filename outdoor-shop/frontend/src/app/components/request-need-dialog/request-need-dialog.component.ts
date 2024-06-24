import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { ItemService } from '../../services/items.service';
import { FormControl, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-request-need-dialog',
  templateUrl: './request-need-dialog.component.html',
  styleUrl: './request-need-dialog.component.scss',
})
export class RequestNeedDialogComponent {
  quantity = new FormControl(1, [Validators.required, Validators.min(1)]);

  constructor(
    @Inject(MAT_DIALOG_DATA) public data: { name: string; id: number },
    public dialogRef: MatDialogRef<RequestNeedDialogComponent>,
    private itemService: ItemService,
    private toastrService: ToastrService
  ) {}

  makeRequest(): void {
    console.log(this.data.id, this.quantity.getRawValue());

    this.itemService
      .requestItems({
        productId: this.data.id,
        quantity: this.quantity.getRawValue() ?? 1,
      })
      .subscribe((response) => {
        this.toastrService.success('Request sent successfully.');
        this.dialogRef.close();
      });
  }
}
