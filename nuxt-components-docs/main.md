<!-- source: https://ui.nuxt.com/components/main --> # MainPRO

[GitHub](https://github.com/nuxt/ui-
pro/blob/v3/src/runtime/components/Main.vue)

A main element that fills the available viewport height.

## Usage

The Main component renders a `<main>` element that works together with the
[Header](/components/header) component to create a full-height layout that
extends to the viewport's available height.

The Header component defines its height through a `--ui-header-height` CSS
variable, which you can customize by overriding it in your CSS:

    
    
    :root {
      --ui-header-height: --spacing(16);
    }
    

## Examples

### Within `app.vue`

Use the Main component in your `app.vue` or in a layout:

app.vue

    
    
    <template>
      <UApp>
        <UHeader />
    
        <UMain>
          <NuxtLayout>
            <NuxtPage />
          </NuxtLayout>
        </UMain>
    
        <UFooter />
      </UApp>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'main'`| `any`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        main: {
          base: 'min-h-[calc(100vh-var(--ui-header-height))]'
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
            main: {
              base: 'min-h-[calc(100vh-var(--ui-header-height))]'
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
            main: {
              base: 'min-h-[calc(100vh-var(--ui-header-height))]'
            }
          }
        })
      ]
    })
    

Expand code

[LocaleSelectA Select to switch between locales.](/components/locale-
select)[ModalA dialog window that can be used to display a message or request
user input.](/components/modal)

