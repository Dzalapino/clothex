import { ChangeDetectionStrategy, Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { FormControl, Validators, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { error } from 'console';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LoginComponent {
  loginForm = new FormGroup({
    login: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required]),
  });

  constructor(
    private authService: AuthService,
    private router: Router,
    private toastr: ToastrService
  ) {}

  signIn(): void {
    const loginValue = this.loginForm.controls.login.value ?? '';
    const passwordValue = this.loginForm.controls.password.value ?? '';
    if (!loginValue || !passwordValue) return;
    this.authService.login(loginValue, passwordValue).subscribe(
      (response) => {
        this.authService.setToken(response.access_token);
        this.router.navigate(['admin']);
        this.toastr.success('Logged in succesfully!');
      },
      (error) => {
        this.toastr.error('Bad credentials!');
      }
    );
  }
}
