<!-- source: https://ui.nuxt.com/components/auth-form --> # AuthFormPRO

[Form](/components/form)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/AuthForm.vue)

A customizable Form to create login, register or password reset forms.

## Usage

Built on top of the [Form](/components/form) component, the `AuthForm`
component can be used in your pages or wrapped in a
[PageCard](/components/page-card).

The form will construct itself based on the `fields` prop and the state will
be handled internally. You can pass all the props you would pass to a
[FormField](/components/form-field#props) or an
[Input](/components/input#props) to each field.

Login

Enter your credentials to access your account.

GoogleGitHub

or

Email

Password

Remember me

Continue

    
    
    <script setup lang="ts">
    import * as z from 'zod'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const toast = useToast()
    
    const fields = [{
      name: 'email',
      type: 'text' as const,
      label: 'Email',
      placeholder: 'Enter your email',
      required: true
    }, {
      name: 'password',
      label: 'Password',
      type: 'password' as const,
      placeholder: 'Enter your password'
    }, {
      name: 'remember',
      label: 'Remember me',
      type: 'checkbox' as const
    }]
    
    const providers = [{
      label: 'Google',
      icon: 'i-simple-icons-google',
      onClick: () => {
        toast.add({ title: 'Google', description: 'Login with Google' })
      }
    }, {
      label: 'GitHub',
      icon: 'i-simple-icons-github',
      onClick: () => {
        toast.add({ title: 'GitHub', description: 'Login with GitHub' })
      }
    }]
    
    const schema = z.object({
      email: z.string().email('Invalid email'),
      password: z.string().min(8, 'Must be at least 8 characters')
    })
    
    type Schema = z.output<typeof schema>
    
    function onSubmit(payload: FormSubmitEvent<Schema>) {
      console.log('Submitted', payload)
    }
    </script>
    
    <template>
      <div class="flex flex-col items-center justify-center gap-4 p-4">
        <UPageCard class="w-full max-w-md">
          <UAuthForm
            :schema="schema"
            title="Login"
            description="Enter your credentials to access your account."
            icon="i-lucide-user"
            :fields="fields"
            :providers="providers"
            @submit="onSubmit"
          />
        </UPageCard>
      </div>
    </template>
    

Expand code

### Title

Use the `title` prop to set the title of the form.

title

Login

Email

Password

Continue

    
    
    <script setup lang="ts">
    const fields = ref([
      {
        name: 'email',
        type: 'text',
        label: 'Email'
      },
      {
        name: 'password',
        type: 'password',
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UAuthForm class="max-w-md" title="Login" :fields="fields" />
    </template>
    

### Description

Use the `description` prop to set the description of the form.

description

Login

Enter your credentials to access your account.

Email

Password

Continue

    
    
    <script setup lang="ts">
    const fields = ref([
      {
        name: 'email',
        type: 'text',
        label: 'Email'
      },
      {
        name: 'password',
        type: 'password',
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UAuthForm
        class="max-w-md"
        title="Login"
        description="Enter your credentials to access your account."
        :fields="fields"
      />
    </template>
    

### Icon

Use the `icon` prop to set the icon of the form.

icon

Login

Enter your credentials to access your account.

Email

Password

Continue

    
    
    <script setup lang="ts">
    const fields = ref([
      {
        name: 'email',
        type: 'text',
        label: 'Email'
      },
      {
        name: 'password',
        type: 'password',
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UAuthForm
        class="max-w-md"
        title="Login"
        description="Enter your credentials to access your account."
        icon="i-lucide-user"
        :fields="fields"
      />
    </template>
    

### Providers

Use the `providers` prop to add providers to the form.

You can pass any property from the [Button](/components/button) component such
as `variant`, `color`, `to`, etc.

Login

Enter your credentials to access your account.

GoogleGitHub

or

Email

Password

Continue

    
    
    <script setup lang="ts">
    const fields = ref([
      {
        name: 'email',
        type: 'text',
        label: 'Email'
      },
      {
        name: 'password',
        type: 'password',
        label: 'Password'
      }
    ])
    const providers = ref([
      {
        label: 'Google',
        icon: 'i-simple-icons-google',
        color: 'neutral',
        variant: 'subtle'
      },
      {
        label: 'GitHub',
        icon: 'i-simple-icons-github',
        color: 'neutral',
        variant: 'subtle'
      }
    ])
    </script>
    
    <template>
      <UAuthForm
        class="max-w-md"
        title="Login"
        description="Enter your credentials to access your account."
        icon="i-lucide-user"
        :providers="providers"
        :fields="fields"
      />
    </template>
    

### Separator

Use the `separator` prop to customize the [Separator](/components/separator)
between the providers and the fields. Defaults to `or`.

separator

Login

Enter your credentials to access your account.

GoogleGitHub

Providers

Email

Password

Continue

    
    
    <script setup lang="ts">
    const providers = ref([
      {
        label: 'Google',
        icon: 'i-simple-icons-google',
        color: 'neutral',
        variant: 'subtle'
      },
      {
        label: 'GitHub',
        icon: 'i-simple-icons-github',
        color: 'neutral',
        variant: 'subtle'
      }
    ])
    const fields = ref([
      {
        name: 'email',
        type: 'text',
        label: 'Email'
      },
      {
        name: 'password',
        type: 'password',
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UAuthForm
        class="max-w-md"
        title="Login"
        description="Enter your credentials to access your account."
        icon="i-lucide-user"
        :providers="providers"
        :fields="fields"
        separator="Providers"
      />
    </template>
    

You can pass any property from the [Separator](/components/separator#props)
component to customize it.

separator.icon

Login

Enter your credentials to access your account.

GoogleGitHub

Email

Password

Continue

    
    
    <script setup lang="ts">
    const providers = ref([
      {
        label: 'Google',
        icon: 'i-simple-icons-google',
        color: 'neutral',
        variant: 'subtle'
      },
      {
        label: 'GitHub',
        icon: 'i-simple-icons-github',
        color: 'neutral',
        variant: 'subtle'
      }
    ])
    const fields = ref([
      {
        name: 'email',
        type: 'text',
        label: 'Email'
      },
      {
        name: 'password',
        type: 'password',
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UAuthForm
        class="max-w-md"
        title="Login"
        description="Enter your credentials to access your account."
        icon="i-lucide-user"
        :providers="providers"
        :fields="fields"
        :separator="{
          icon: 'i-lucide-user'
        }"
      />
    </template>
    

### Submit

Use the `submit` prop to change the submit button of the form.

You can pass any property from the [Button](/components/button) component such
as `variant`, `color`, `to`, etc.

Login

Enter your credentials to access your account.

Email

Password

Submit

    
    
    <script setup lang="ts">
    const fields = ref([
      {
        name: 'email',
        type: 'text',
        label: 'Email'
      },
      {
        name: 'password',
        type: 'password',
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UAuthForm
        class="max-w-md"
        title="Login"
        description="Enter your credentials to access your account."
        icon="i-lucide-user"
        :fields="fields"
        :submit="{
          label: 'Submit',
          color: 'error',
          variant: 'subtle'
        }"
      />
    </template>
    

## Examples

### Within a page

You can wrap the `AuthForm` component with the [PageCard](/components/page-
card) component to display it within a `login.vue` page for example.

Welcome back!

Don't have an account? Sign up.

GoogleGitHub

or

Email

PasswordForgot password?

Remember me

Error signing in

Continue

By signing in, you agree to our Terms of Service.

    
    
    <script setup lang="ts">
    import * as z from 'zod'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const toast = useToast()
    
    const fields = [{
      name: 'email',
      type: 'text' as const,
      label: 'Email',
      placeholder: 'Enter your email',
      required: true
    }, {
      name: 'password',
      label: 'Password',
      type: 'password' as const,
      placeholder: 'Enter your password'
    }, {
      name: 'remember',
      label: 'Remember me',
      type: 'checkbox' as const
    }]
    
    const providers = [{
      label: 'Google',
      icon: 'i-simple-icons-google',
      onClick: () => {
        toast.add({ title: 'Google', description: 'Login with Google' })
      }
    }, {
      label: 'GitHub',
      icon: 'i-simple-icons-github',
      onClick: () => {
        toast.add({ title: 'GitHub', description: 'Login with GitHub' })
      }
    }]
    
    const schema = z.object({
      email: z.string().email('Invalid email'),
      password: z.string().min(8, 'Must be at least 8 characters')
    })
    
    type Schema = z.output<typeof schema>
    
    function onSubmit(payload: FormSubmitEvent<Schema>) {
      console.log('Submitted', payload)
    }
    </script>
    
    <template>
      <div class="flex flex-col items-center justify-center gap-4 p-4">
        <UPageCard class="w-full max-w-md">
          <UAuthForm
            :schema="schema"
            :fields="fields"
            :providers="providers"
            title="Welcome back!"
            icon="i-lucide-lock"
            @submit="onSubmit"
          >
            <template #description>
              Don't have an account? <ULink to="#" class="text-primary font-medium">Sign up</ULink>.
            </template>
            <template #password-hint>
              <ULink to="#" class="text-primary font-medium" tabindex="-1">Forgot password?</ULink>
            </template>
            <template #validation>
              <UAlert color="error" icon="i-lucide-info" title="Error signing in" />
            </template>
            <template #footer>
              By signing in, you agree to our <ULink to="#" class="text-primary font-medium">Terms of Service</ULink>.
            </template>
          </UAuthForm>
        </UPageCard>
      </div>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`icon`| | ` string`The icon displayed above the title.  
`title`| | ` string`  
`description`| | ` string`  
`fields`| | ` AuthFormField[]`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `name: string`The name of the FormField. Also used to match form errors.
  * `errorPattern?: RegExp`A regular expression to match form error names.
  * `label?: string`
  * `description?: string`
  * `help?: string`
  * `error?: string | boolean`
  * `hint?: string`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `required?: boolean`
  * `eagerValidation?: boolean`If true, validation on input will be active immediately instead of waiting for a blur event.
  * `validateOnInputDelay?: number`Delay in milliseconds before validating the form on input events. Defaults to `300`.
  * `class?: any`
  * `ui?: { root?: ClassNameValue; wrapper?: ClassNameValue; labelWrapper?: ClassNameValue; label?: ClassNameValue; container?: ClassNameValue; description?: ClassNameValue; error?: ClassNameValue; hint?: ClassNameValue; help?: ClassNameValue; }`
  * `type?: "select" | "text" | "checkbox" | "password"`
  * `defaultValue?: any`

  
`providers`| | ` ButtonProps[]`Display a list of Button under the description. `{ color: 'neutral', variant: 'subtle', block: true }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.

  
`separator`| `'or'`| ` string | SeparatorProps`The text displayed in the separator.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `label?: string`Display a label in the middle.
  * `icon?: string`Display an icon in the middle.
  * `avatar?: AvatarProps`Display an avatar in the middle.
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'neutral'`.
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'xs'`.
  * `type?: "solid" | "dashed" | "dotted"`Defaults to `'solid'`.
  * `orientation?: DataOrientation`The orientation of the separator. Defaults to `'horizontal'`.
  * `class?: any`
  * `ui?: { root?: ClassNameValue; border?: ClassNameValue; container?: ClassNameValue; icon?: ClassNameValue; avatar?: ClassNameValue; avatarSize?: ClassNameValue; label?: ClassNameValue; }`
  * `decorative?: boolean`Whether or not the component is purely decorative.   
When `true`, accessibility-related attributes are updated so that that the
rendered element is removed from the accessibility tree.

  
`submit`| | ` ButtonProps`Display a submit button at the bottom of the form. `{ label: 'Continue', block: true }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.

  
`schema`| | ` Struct<any, any> | ObjectSchema<object, AnyObject, any, ""> | AnySchema<object> | ArraySchema<object> | AlternativesSchema<object> | BinarySchema<object> | BooleanSchema<object> | DateSchema<object> | FunctionSchema<object> | NumberSchema<object> | ObjectSchema<object> | StringSchema<object> | LinkSchema<object> | SymbolSchema<object> | StandardSchemaV1<object, object>`  
`validate`| | ` (state: Partial<any>): FormError<string>[] | Promise<FormError<string>[]>`  
`validateOn`| | ` FormInputEvents[]`  
`validateOnInputDelay`| | ` number`  
`disabled`| | `boolean`  
`loading`| | `boolean`  
`ui`| | ` { root?: ClassNameValue; header?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; title?: ClassNameValue; ... 5 more ...; footer?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`header`| `{}`  
`leading`| `{}`  
`title`| `{}`  
`description`| `{}`  
`validation`| `{}`  
`footer`| `{}`  
  
### Emits

Event |  Type   
---|---  
`submit`| `FormSubmitEvent<any>`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        authForm: {
          slots: {
            root: 'w-full space-y-6',
            header: 'flex flex-col text-center',
            leading: 'mb-2',
            leadingIcon: 'size-8 shrink-0',
            title: 'text-xl text-pretty font-semibold text-highlighted',
            description: 'mt-1 text-base text-pretty text-muted',
            body: 'gap-y-6 flex flex-col',
            providers: 'space-y-3',
            separator: '',
            form: 'space-y-5',
            footer: 'text-sm text-center text-muted mt-2'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            authForm: {
              slots: {
                root: 'w-full space-y-6',
                header: 'flex flex-col text-center',
                leading: 'mb-2',
                leadingIcon: 'size-8 shrink-0',
                title: 'text-xl text-pretty font-semibold text-highlighted',
                description: 'mt-1 text-base text-pretty text-muted',
                body: 'gap-y-6 flex flex-col',
                providers: 'space-y-3',
                separator: '',
                form: 'space-y-5',
                footer: 'text-sm text-center text-muted mt-2'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            authForm: {
              slots: {
                root: 'w-full space-y-6',
                header: 'flex flex-col text-center',
                leading: 'mb-2',
                leadingIcon: 'size-8 shrink-0',
                title: 'text-xl text-pretty font-semibold text-highlighted',
                description: 'mt-1 text-base text-pretty text-muted',
                body: 'gap-y-6 flex flex-col',
                providers: 'space-y-3',
                separator: '',
                form: 'space-y-5',
                footer: 'text-sm text-center text-muted mt-2'
              }
            }
          }
        })
      ]
    })
    

Expand code

[AlertA callout to draw user's attention.](/components/alert)[AvatarAn img
element with fallback and Nuxt Image support.](/components/avatar)

