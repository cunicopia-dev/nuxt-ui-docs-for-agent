<!-- source: https://ui.nuxt.com/components/container --> # Container

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Container.vue)

A container lets you center and constrain the width of your content.

## Usage

    
    
    <template>
      <UContainer>
        <Placeholder class="h-32" />
      </UContainer>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        container: {
          base: 'w-full max-w-(--ui-container) mx-auto px-4 sm:px-6 lg:px-8'
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
            container: {
              base: 'w-full max-w-(--ui-container) mx-auto px-4 sm:px-6 lg:px-8'
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
            container: {
              base: 'w-full max-w-(--ui-container) mx-auto px-4 sm:px-6 lg:px-8'
            }
          }
        })
      ]
    })
    

Expand code

[CommandPaletteA command palette with full-text search powered by Fuse.js for
efficient fuzzy matching.](/components/command-palette)[ContextMenuA menu to
display actions when right-clicking on an element.](/components/context-menu)

