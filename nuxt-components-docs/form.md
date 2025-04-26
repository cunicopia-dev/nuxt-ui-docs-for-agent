<!-- source: https://ui.nuxt.com/components/form --> # Form

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Form.vue)

A form component with built-in validation and submission handling.

## Usage

Use the Form component to validate form data using validation libraries such
as [Valibot](https://github.com/fabian-hiller/valibot),
[Zod](https://github.com/colinhacks/zod),
[Yup](https://github.com/jquense/yup), [Joi](https://github.com/hapijs/joi),
[Superstruct](https://github.com/ianstormtaylor/superstruct) or your own
validation logic.

It works with the [FormField](/components/form-field) component to display
error messages around form elements automatically.

### Schema Validation

It requires two props:

  * `state` \- a reactive object holding the form's state.
  * `schema` \- any [Standard Schema](https://standardschema.dev/) or a schema from [Yup](https://github.com/jquense/yup), [Joi](https://github.com/hapijs/joi) or [Superstruct](https://github.com/ianstormtaylor/superstruct).

**No validation library is included** by default, ensure you **install the one
you need**.

ValibotZodYupJoiSuperstruct

Email

Password

Submit

    
    
    <script setup lang="ts">
    import * as v from 'valibot'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const schema = v.object({
      email: v.pipe(v.string(), v.email('Invalid email')),
      password: v.pipe(v.string(), v.minLength(8, 'Must be at least 8 characters'))
    })
    
    type Schema = v.InferOutput<typeof schema>
    
    const state = reactive({
      email: '',
      password: ''
    })
    
    const toast = useToast()
    async function onSubmit(event: FormSubmitEvent<Schema>) {
      toast.add({ title: 'Success', description: 'The form has been submitted.', color: 'success' })
      console.log(event.data)
    }
    </script>
    
    <template>
      <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
        <UFormField label="Email" name="email">
          <UInput v-model="state.email" />
        </UFormField>
    
        <UFormField label="Password" name="password">
          <UInput v-model="state.password" type="password" />
        </UFormField>
    
        <UButton type="submit">
          Submit
        </UButton>
      </UForm>
    </template>
    

Email

Password

Submit

    
    
    <script setup lang="ts">
    import * as z from 'zod'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const schema = z.object({
      email: z.string().email('Invalid email'),
      password: z.string().min(8, 'Must be at least 8 characters')
    })
    
    type Schema = z.output<typeof schema>
    
    const state = reactive<Partial<Schema>>({
      email: undefined,
      password: undefined
    })
    
    const toast = useToast()
    async function onSubmit(event: FormSubmitEvent<Schema>) {
      toast.add({ title: 'Success', description: 'The form has been submitted.', color: 'success' })
      console.log(event.data)
    }
    </script>
    
    <template>
      <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
        <UFormField label="Email" name="email">
          <UInput v-model="state.email" />
        </UFormField>
    
        <UFormField label="Password" name="password">
          <UInput v-model="state.password" type="password" />
        </UFormField>
    
        <UButton type="submit">
          Submit
        </UButton>
      </UForm>
    </template>
    

Email

Password

Submit

    
    
    <script setup lang="ts">
    import { object, string, type InferType } from 'yup'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const schema = object({
      email: string().email('Invalid email').required('Required'),
      password: string()
        .min(8, 'Must be at least 8 characters')
        .required('Required')
    })
    
    type Schema = InferType<typeof schema>
    
    const state = reactive({
      email: undefined,
      password: undefined
    })
    
    const toast = useToast()
    async function onSubmit(event: FormSubmitEvent<Schema>) {
      toast.add({ title: 'Success', description: 'The form has been submitted.', color: 'success' })
      console.log(event.data)
    }
    </script>
    
    <template>
      <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
        <UFormField label="Email" name="email">
          <UInput v-model="state.email" />
        </UFormField>
    
        <UFormField label="Password" name="password">
          <UInput v-model="state.password" type="password" />
        </UFormField>
    
        <UButton type="submit">
          Submit
        </UButton>
      </UForm>
    </template>
    

Email

Password

Submit

    
    
    <script setup lang="ts">
    import Joi from 'joi'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const schema = Joi.object({
      email: Joi.string().required(),
      password: Joi.string()
        .min(8)
        .required()
    })
    
    const state = reactive({
      email: undefined,
      password: undefined
    })
    
    const toast = useToast()
    async function onSubmit(event: FormSubmitEvent<typeof state>) {
      toast.add({ title: 'Success', description: 'The form has been submitted.', color: 'success' })
      console.log(event.data)
    }
    </script>
    
    <template>
      <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
        <UFormField label="Email" name="email">
          <UInput v-model="state.email" />
        </UFormField>
    
        <UFormField label="Password" name="password">
          <UInput v-model="state.password" type="password" />
        </UFormField>
    
        <UButton type="submit">
          Submit
        </UButton>
      </UForm>
    </template>
    

Email

Password

Submit

    
    
    <script setup lang="ts">
    import { object, string, nonempty, refine, type Infer } from 'superstruct'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const schema = object({
      email: nonempty(string()),
      password: refine(string(), 'Password', (value) => {
        if (value.length >= 8) return true
        return 'Must be at least 8 characters'
      })
    })
    
    const state = reactive({
      email: '',
      password: ''
    })
    
    type Schema = Infer<typeof schema>
    
    async function onSubmit(event: FormSubmitEvent<Schema>) {
      console.log(event.data)
    }
    </script>
    
    <template>
      <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
        <UFormField label="Email" name="email">
          <UInput v-model="state.email" />
        </UFormField>
    
        <UFormField label="Password" name="password">
          <UInput v-model="state.password" type="password" />
        </UFormField>
    
        <UButton type="submit">
          Submit
        </UButton>
      </UForm>
    </template>
    

Errors are reported directly to the [FormField](/components/form-field)
component based on the `name` or `error-pattern` prop. This means the
validation rules defined for the `email` attribute in your schema will be
applied to `<FormField name="email">`.

Nested validation rules are handled using dot notation. For example, a rule
like `{ user: z.object({ email: z.string() }) }` will be applied to
`<FormField name="user.email">`.

### Custom Validation

Use the `validate` prop to apply your own validation logic.

The validation function must return a list of errors with the following
attributes:

  * `message` \- the error message to display.
  * `name` \- the `name` of the `FormField` to send the error to.

It can be used alongside the `schema` prop to handle complex use cases.

Email

Password

Submit

    
    
    <script setup lang="ts">
    import type { FormError, FormSubmitEvent } from '@nuxt/ui'
    
    const state = reactive({
      email: undefined,
      password: undefined
    })
    
    const validate = (state: any): FormError[] => {
      const errors = []
      if (!state.email) errors.push({ name: 'email', message: 'Required' })
      if (!state.password) errors.push({ name: 'password', message: 'Required' })
      return errors
    }
    
    const toast = useToast()
    async function onSubmit(event: FormSubmitEvent<typeof state>) {
      toast.add({ title: 'Success', description: 'The form has been submitted.', color: 'success' })
      console.log(event.data)
    }
    </script>
    
    <template>
      <UForm :validate="validate" :state="state" class="space-y-4" @submit="onSubmit">
        <UFormField label="Email" name="email">
          <UInput v-model="state.email" />
        </UFormField>
    
        <UFormField label="Password" name="password">
          <UInput v-model="state.password" type="password" />
        </UFormField>
    
        <UButton type="submit">
          Submit
        </UButton>
      </UForm>
    </template>
    

### Input Events

The Form component automatically triggers validation when an input emits an
`input`, `change`, or `blur` event.

  * Validation on `input` occurs **as you type**.
  * Validation on `change` occurs when you **commit to a value**.
  * Validation on `blur` happens when an input **loses focus**.

You can control when validation happens this using the `validate-on` prop.

validate-on

input, change, blur

Input

Switch me

Check me

Slider

Select

Select Menu

Select Menu (Multiple)

Input Menu

Input Menu (Multiple)

Input Number

Textarea

Radio group

Option 1

Option 2

Option 3

Checkbox group

Option 1

Option 2

Option 3

Pin Input

Submit  Clear

You can use the [`useFormField`](/composables/use-form-field) composable to
implement this inside your own components.

### Error Event

You can listen to the `@error` event to handle errors. This event is triggered
when the form is submitted and contains an array of `FormError` objects with
the following fields:

  * `id` \- the input's `id`.
  * `name` \- the `name` of the `FormField`
  * `message` \- the error message to display.

Here's an example that focuses the first input element with an error after the
form is submitted:

Email

Password

Submit

    
    
    <script setup lang="ts">
    import type { FormError, FormErrorEvent, FormSubmitEvent } from '@nuxt/ui'
    
    const state = reactive({
      email: undefined,
      password: undefined
    })
    
    const validate = (state: any): FormError[] => {
      const errors = []
      if (!state.email) errors.push({ name: 'email', message: 'Required' })
      if (!state.password) errors.push({ name: 'password', message: 'Required' })
      return errors
    }
    
    const toast = useToast()
    async function onSubmit(event: FormSubmitEvent<typeof state>) {
      toast.add({ title: 'Success', description: 'The form has been submitted.', color: 'success' })
      console.log(event.data)
    }
    
    async function onError(event: FormErrorEvent) {
      if (event?.errors?.[0]?.id) {
        const element = document.getElementById(event.errors[0].id)
        element?.focus()
        element?.scrollIntoView({ behavior: 'smooth', block: 'center' })
      }
    }
    </script>
    
    <template>
      <UForm :validate="validate" :state="state" class="space-y-4" @submit="onSubmit" @error="onError">
        <UFormField label="Email" name="email">
          <UInput v-model="state.email" />
        </UFormField>
    
        <UFormField label="Password" name="password">
          <UInput v-model="state.password" type="password" />
        </UFormField>
    
        <UButton type="submit">
          Submit
        </UButton>
      </UForm>
    </template>
    

Expand code

### Nesting Forms

Nesting form components allows you to manage complex data structures, such as
lists or conditional fields, more efficiently.

For example, it can be used to dynamically add fields based on user's input:

Name

Register to our newsletter

Submit

    
    
    <script setup lang="ts">
    import * as z from 'zod'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const schema = z.object({
      name: z.string().min(2),
      news: z.boolean().default(false)
    })
    
    type Schema = z.output<typeof schema>
    
    const nestedSchema = z.object({
      email: z.string().email()
    })
    
    type NestedSchema = z.output<typeof nestedSchema>
    
    const state = reactive<Partial<Schema & NestedSchema>>({ })
    
    const toast = useToast()
    async function onSubmit(event: FormSubmitEvent<Schema>) {
      toast.add({ title: 'Success', description: 'The form has been submitted.', color: 'success' })
      console.log(event.data)
    }
    </script>
    
    <template>
      <UForm
        :state="state"
        :schema="schema"
        class="gap-4 flex flex-col w-60"
        @submit="onSubmit"
      >
        <UFormField label="Name" name="name">
          <UInput v-model="state.name" placeholder="John Lennon" />
        </UFormField>
    
        <div>
          <UCheckbox v-model="state.news" name="news" label="Register to our newsletter" @update:model-value="state.email = undefined" />
        </div>
    
        <UForm v-if="state.news" :state="state" :schema="nestedSchema" attach>
          <UFormField label="Email" name="email">
            <UInput v-model="state.email" placeholder="[[email protected]](/cdn-cgi/l/email-protection)" />
          </UFormField>
        </UForm>
    
        <div>
          <UButton type="submit">
            Submit
          </UButton>
        </div>
      </UForm>
    </template>
    

Expand code

Or to validate list inputs:

Customer

Description

Price

Add Item  Remove Item

Submit

    
    
    <script setup lang="ts">
    import * as z from 'zod'
    import type { FormSubmitEvent } from '@nuxt/ui'
    
    const schema = z.object({
      customer: z.string().min(2)
    })
    
    type Schema = z.output<typeof schema>
    
    const itemSchema = z.object({
      description: z.string().min(1),
      price: z.number().min(0)
    })
    
    type ItemSchema = z.output<typeof itemSchema>
    
    const state = reactive<Partial<Schema & { items: Partial<ItemSchema>[] }>>({
      items: [{}]
    })
    
    function addItem() {
      if (!state.items) {
        state.items = []
      }
      state.items.push({})
    }
    
    function removeItem() {
      if (state.items) {
        state.items.pop()
      }
    }
    
    const toast = useToast()
    
    async function onSubmit(event: FormSubmitEvent<Schema>) {
      toast.add({ title: 'Success', description: 'The form has been submitted.', color: 'success' })
      console.log(event.data)
    }
    </script>
    
    <template>
      <UForm
        :state="state"
        :schema="schema"
        class="gap-4 flex flex-col w-60"
        @submit="onSubmit"
      >
        <UFormField label="Customer" name="customer">
          <UInput v-model="state.customer" placeholder="Wonka Industries" />
        </UFormField>
    
        <UForm
          v-for="item, count in state.items"
          :key="count"
          :state="item"
          :schema="itemSchema"
          attach
          class="flex gap-2"
        >
          <UFormField :label="!count ? 'Description' : undefined" name="description">
            <UInput v-model="item.description" />
          </UFormField>
          <UFormField :label="!count ? 'Price' : undefined" name="price" class="w-20">
            <UInput v-model="item.price" type="number" />
          </UFormField>
        </UForm>
    
        <div class="flex gap-2">
          <UButton color="neutral" variant="subtle" size="sm" @click="addItem()">
            Add Item
          </UButton>
    
          <UButton color="neutral" variant="ghost" size="sm" @click="removeItem()">
            Remove Item
          </UButton>
        </div>
        <div>
          <UButton type="submit">
            Submit
          </UButton>
        </div>
      </UForm>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`state`| | `Partial<any>`An object representing the current state of the form.  
`id`| | ` string | number`  
`schema`| | ` Struct<any, any> | ObjectSchema<object, AnyObject, any, ""> | AnySchema<object> | ArraySchema<object> | AlternativesSchema<object> | BinarySchema<object> | BooleanSchema<object> | DateSchema<object> | FunctionSchema<object> | NumberSchema<object> | ObjectSchema<object> | StringSchema<object> | LinkSchema<object> | SymbolSchema<object> | StandardSchemaV1<object, object>`Schema to validate the form state. Supports Standard Schema objects, Yup, Joi, and Superstructs.  
`validate`| | ` (state: Partial<any>): FormError<string>[] | Promise<FormError<string>[]>`Custom validation function to validate the form state.  
`validateOn`| `['blur', 'change', 'input']`| ` FormInputEvents[]`The list of
input events that trigger the form validation.  
`disabled`| | `boolean`Disable all inputs inside the form.  
`validateOnInputDelay`| `300`| ` number`Delay in milliseconds before
validating the form on input events.  
`transform`| `true`| `boolean`If true, schema transformations will be applied
to the state on submit.  
`attach`| `true`| `boolean`If true, this form will attach to its parent Form
(if any) and validate at the same time.  
`loadingAuto`| `true`| `boolean`When `true`, all form elements will be
disabled on `@submit` event. This will cause any focused input elements to
lose their focus state.  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ errors: FormError<string>[]; }`  
  
### Emits

Event |  Type   
---|---  
`submit`| `FormSubmitEvent<any>`  
`error`| `FormErrorEvent`  
  
### Expose

You can access the typed component instance using
[`useTemplateRef`](https://vuejs.org/api/composition-api-
helpers.html#usetemplateref).

    
    
    <script setup lang="ts">
    const form = useTemplateRef('form')
    </script>
    
    <template>
      <UForm ref="form" />
    </template>
    

This will give you access to the following:

Name| Type  
---|---  
`submit()`| `Promise<void>`  
Triggers form submission.  
`validate(opts: { name?: keyof T | (keyof T)[], silent?: boolean, nested?: boolean, transform?: boolean })`| `Promise<T>`   
Triggers form validation. Will raise any errors unless `opts.silent` is set to
true.  
`clear(path?: keyof T)`| `void`  
Clears form errors associated with a specific path. If no path is provided,
clears all form errors.  
`getErrors(path?: keyof T)`| `FormError[]`  
Retrieves form errors associated with a specific path. If no path is provided,
returns all form errors.  
`setErrors(errors: FormError[], name?: keyof T)`| `void`  
Sets form errors for a given path. If no path is provided, overrides all
errors.  
`errors`| `Ref<FormError[]>`  
A reference to the array containing validation errors. Use this to access or
manipulate the error information.  
`disabled`| `Ref<boolean>`  
`dirty`| `Ref<boolean>` `true` if at least one form field has been updated by
the user.  
`dirtyFields`| `DeepReadonly<Set<keyof T>>` Tracks fields that have been
modified by the user.  
`touchedFields`| `DeepReadonly<Set<keyof T>>` Tracks fields that the user
interacted with.  
`blurredFields`| `DeepReadonly<Set<keyof T>>` Tracks fields blurred by the
user.  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        form: {
          base: ''
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
          ui: {
            form: {
              base: ''
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
          ui: {
            form: {
              base: ''
            }
          }
        })
      ]
    })
    

Expand code

[DropdownMenuA menu to display actions when clicking on an
element.](/components/dropdown-menu)[FormFieldA wrapper for form elements that
provides validation and error handling.](/components/form-field)

