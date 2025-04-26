<!-- source: https://ui.nuxt.com/components/skeleton --> # Skeleton

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Skeleton.vue)

A placeholder to show while content is loading.

## Usage

    
    
    <template>
      <div class="flex items-center gap-4">
        <USkeleton class="h-12 w-12 rounded-full" />
    
        <div class="grid gap-2">
          <USkeleton class="h-4 w-[250px]" />
          <USkeleton class="h-4 w-[200px]" />
        </div>
      </div>
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
        skeleton: {
          base: 'animate-pulse rounded-md bg-elevated'
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
            skeleton: {
              base: 'animate-pulse rounded-md bg-elevated'
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
            skeleton: {
              base: 'animate-pulse rounded-md bg-elevated'
            }
          }
        })
      ]
    })
    

Expand code

[SeparatorSeparates content horizontally or
vertically.](/components/separator)[SlideoverA dialog that slides in from any
side of the screen.](/components/slideover)

