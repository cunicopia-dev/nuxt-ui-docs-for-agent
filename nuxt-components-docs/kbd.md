<!-- source: https://ui.nuxt.com/components/kbd --> # Keyboard Key

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Kbd.vue)

A kbd element to display a keyboard key.

## Usage

### Value

Use the default slot to set the value of the Kbd.

    
    
    <template>
      <UKbd>K</UKbd>
    </template>
    

You can achieve the same result by using the `value` prop.

value

    
    
    <template>
      <UKbd value="K" />
    </template>
    

You can pass special keys to the `value` prop that goes through the
[`useKbd`](https://github.com/nuxt/ui/blob/v3/src/runtime/composables/useKbd.ts)
composable. For example, the `meta` key displays as `⌘` on macOS and `⊞` on
other platforms.

value

meta

    
    
    <template>
      <UKbd value="meta" />
    </template>
    

### Variant

Use the `variant` prop to change the variant of the Kbd.

variant

solid

    
    
    <template>
      <UKbd variant="solid">K</UKbd>
    </template>
    

### Size

Use the `size` prop to change the size of the Kbd.

size

lg

    
    
    <template>
      <UKbd size="lg">K</UKbd>
    </template>
    

## Examples

### `class` prop

Use the `class` prop to override the base styles of the Badge.

class

variant

subtle

    
    
    <template>
      <UKbd class="font-bold rounded-full" variant="subtle">K</UKbd>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'kbd'`| `any`The element or component this component should render as.  
`value`| | ` string`  
`variant`| `'outline'`| ` "outline" | "subtle" | "solid"`  
`size`| `'md'`| ` "sm" | "md" | "lg"`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        kbd: {
          base: 'inline-flex items-center justify-center px-1 rounded-sm font-medium font-sans',
          variants: {
            variant: {
              solid: 'bg-inverted text-inverted',
              outline: 'bg-default text-highlighted ring ring-inset ring-accented',
              subtle: 'bg-elevated text-default ring ring-inset ring-accented'
            },
            size: {
              sm: 'h-4 min-w-[16px] text-[10px]',
              md: 'h-5 min-w-[20px] text-[11px]',
              lg: 'h-6 min-w-[24px] text-[12px]'
            }
          },
          defaultVariants: {
            variant: 'outline',
            size: 'md'
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
          ui: {
            kbd: {
              base: 'inline-flex items-center justify-center px-1 rounded-sm font-medium font-sans',
              variants: {
                variant: {
                  solid: 'bg-inverted text-inverted',
                  outline: 'bg-default text-highlighted ring ring-inset ring-accented',
                  subtle: 'bg-elevated text-default ring ring-inset ring-accented'
                },
                size: {
                  sm: 'h-4 min-w-[16px] text-[10px]',
                  md: 'h-5 min-w-[20px] text-[11px]',
                  lg: 'h-6 min-w-[24px] text-[12px]'
                }
              },
              defaultVariants: {
                variant: 'outline',
                size: 'md'
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
          ui: {
            kbd: {
              base: 'inline-flex items-center justify-center px-1 rounded-sm font-medium font-sans',
              variants: {
                variant: {
                  solid: 'bg-inverted text-inverted',
                  outline: 'bg-default text-highlighted ring ring-inset ring-accented',
                  subtle: 'bg-elevated text-default ring ring-inset ring-accented'
                },
                size: {
                  sm: 'h-4 min-w-[16px] text-[10px]',
                  md: 'h-5 min-w-[20px] text-[11px]',
                  lg: 'h-6 min-w-[24px] text-[12px]'
                }
              },
              defaultVariants: {
                variant: 'outline',
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[InputNumberInput numerical values with a customizable
range.](/components/input-number)[LinkA wrapper around <NuxtLink> with extra
props.](/components/link)

