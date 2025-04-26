<!-- source: https://ui.nuxt.com/components/error --> # ErrorPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/Error.vue)

A pre-built error component with NuxtError support.

## Usage

Like the [Main](/components/main) component, the Error component renders a
`<main>` element that works together with the [Header](/components/header)
component to create a full-height layout that extends to the viewport's
available height.

The Header component defines its height through a `--ui-header-height` CSS
variable, which you can customize by overriding it in your CSS:

    
    
    :root {
      --ui-header-height: --spacing(16);
    }
    

### Error

Use the `error` prop to display an error message.

[](https://nuxt.com/docs/guide/directory-structure/error)In most cases, you
will receive the `error` prop in your `error.vue` file.

error.statusCode

error.statusMessage

error.message

    
    
    <template>
      <UError
        :error="{
          statusCode: 404,
          statusMessage: 'Page not found',
          message: 'The page you are looking for does not exist.'
        }"
      />
    </template>
    

### Clear

Use the `clear` prop to customize or hide the clear button (with `false`
value).

You can pass any property from the [Button](/components/button) component to
customize it.

    
    
    <template>
      <UError
        :clear="{
          color: 'neutral',
          size: 'xl',
          icon: 'i-lucide-arrow-left',
          class: 'rounded-full'
        }"
        :error="{
          statusCode: 404,
          statusMessage: 'Page not found',
          message: 'The page you are looking for does not exist.'
        }"
      />
    </template>
    

### Redirect

Use the `redirect` prop to redirect the user to a different page when the
clear button is clicked. Defaults to `/`.

redirect

    
    
    <template>
      <UError
        redirect="/getting-started"
        :error="{
          statusCode: 404,
          statusMessage: 'Page not found',
          message: 'The page you are looking for does not exist.'
        }"
      />
    </template>
    

## Examples

### Within `error.vue`

Use the Error component in your `error.vue`:

error.vue

    
    
    <script setup lang="ts">
    import type { NuxtError } from '#app'
    
    const props = defineProps<{
      error: NuxtError
    }>()
    </script>
    
    <template>
      <UApp>
        <UHeader />
    
        <UError :error="error" />
    
        <UFooter />
      </UApp>
    </template>
    

You might want to replicate the code of your `app.vue` inside your `error.vue`
file to have the same layout and features, here is an example:
<https://github.com/nuxt/ui/blob/v3/docs/app/error.vue>

You can read more about how to handle errors in the [Nuxt
documentation](https://nuxt.com/docs/getting-started/error-handling#error-
page), but when using `nuxt generate` it is recommended to add `fatal: true`
inside your `createError` call to make sure the error page is displayed:

pages/[...slug].vue

    
    
    <script setup lang="ts">
    const route = useRoute()
    
    const { data: page } = await useAsyncData(route.path, () => queryContent(route.path).findOne())
    if (!page.value) {
      throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
    }
    </script>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'main'`| `any`  
`clear`| `true`| `boolean | Partial<ButtonProps>`  
`redirect`| `'/'`| ` string`  
`error`| | ` Partial<NuxtError<unknown> & { message: string; }>`  
`ui`| | ` { root?: ClassNameValue; statusCode?: ClassNameValue; statusMessage?: ClassNameValue; message?: ClassNameValue; links?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`statusCode`| `{}`  
`statusMessage`| `{}`  
`links`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        error: {
          slots: {
            root: 'min-h-[calc(100vh-var(--ui-header-height))] flex flex-col items-center justify-center text-center',
            statusCode: 'text-base font-semibold text-primary',
            statusMessage: 'mt-2 text-4xl sm:text-5xl font-bold text-highlighted text-balance',
            message: 'mt-4 text-lg text-muted text-balance',
            links: 'mt-8 flex items-center justify-center gap-6'
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
            error: {
              slots: {
                root: 'min-h-[calc(100vh-var(--ui-header-height))] flex flex-col items-center justify-center text-center',
                statusCode: 'text-base font-semibold text-primary',
                statusMessage: 'mt-2 text-4xl sm:text-5xl font-bold text-highlighted text-balance',
                message: 'mt-4 text-lg text-muted text-balance',
                links: 'mt-8 flex items-center justify-center gap-6'
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
            error: {
              slots: {
                root: 'min-h-[calc(100vh-var(--ui-header-height))] flex flex-col items-center justify-center text-center',
                statusCode: 'text-base font-semibold text-primary',
                statusMessage: 'mt-2 text-4xl sm:text-5xl font-bold text-highlighted text-balance',
                message: 'mt-4 text-lg text-muted text-balance',
                links: 'mt-8 flex items-center justify-center gap-6'
              }
            }
          }
        })
      ]
    })
    

Expand code

[DropdownMenuA menu to display actions when clicking on an
element.](/components/dropdown-menu)[FooterA responsive footer
component.](/components/footer)

