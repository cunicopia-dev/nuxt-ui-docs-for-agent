<!-- source: https://ui.nuxt.com/components/color-picker --> # ColorPicker

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/ColorPicker.vue)

A component to select a color.

## Usage

Use the `v-model` directive to control the value of the ColorPicker.

    
    
    <script setup lang="ts">
    const value = ref('#00C16A')
    </script>
    
    <template>
      <UColorPicker v-model="value" />
    </template>
    

Use the `default-value` prop to set the initial value when you do not need to
control its state.

    
    
    <template>
      <UColorPicker default-value="#00BCD4" />
    </template>
    

### RGB Format

Use the `format` prop to set `rgb` value of the ColorPicker.

    
    
    <script setup lang="ts">
    const value = ref('rgb(0, 193, 106)')
    </script>
    
    <template>
      <UColorPicker format="rgb" v-model="value" />
    </template>
    

### HSL Format

Use the `format` prop to set `hsl` value of the ColorPicker.

    
    
    <script setup lang="ts">
    const value = ref('hsl(153, 100%, 37.8%)')
    </script>
    
    <template>
      <UColorPicker format="hsl" v-model="value" />
    </template>
    

### CMYK Format

Use the `format` prop to set `cmyk` value of the ColorPicker.

    
    
    <script setup lang="ts">
    const value = ref('cmyk(100%, 0%, 45.08%, 24.31%)')
    </script>
    
    <template>
      <UColorPicker format="cmyk" v-model="value" />
    </template>
    

### CIELab Format

Use the `format` prop to set `lab` value of the ColorPicker.

    
    
    <script setup lang="ts">
    const value = ref('lab(68.88% -60.41% 32.55%)')
    </script>
    
    <template>
      <UColorPicker format="lab" v-model="value" />
    </template>
    

### Throttle

Use the `throttle` prop to set the throttle value of the ColorPicker.

throttle

    
    
    <script setup lang="ts">
    const value = ref('#00C16A')
    </script>
    
    <template>
      <UColorPicker :throttle="100" v-model="value" />
    </template>
    

### Size

Use the `size` prop to set the size of the ColorPicker.

size

xl

    
    
    <template>
      <UColorPicker size="xl" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the ColorPicker.

disabled

true

    
    
    <template>
      <UColorPicker disabled />
    </template>
    

## Examples

### As a Color chooser

Use a [Button](/components/button) and a [Popover](/components/popover)
component to create a color chooser.

Choose color

    
    
    <script setup lang="ts">
    const color = ref('#00C16A')
    
    const chip = computed(() => ({ backgroundColor: color.value }))
    </script>
    
    <template>
      <UPopover>
        <UButton label="Choose color" color="neutral" variant="outline">
          <template #leading>
            <span :style="chip" class="size-3 rounded-full" />
          </template>
        </UButton>
    
        <template #content>
          <UColorPicker v-model="color" class="p-2" />
        </template>
      </UPopover>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`throttle`| `50`| ` number`Throttle time in ms for the color picker  
`disabled`| | `boolean`Disable the color picker  
`defaultValue`| `'#FFFFFF'`| ` string`The default value of the color picker  
`format`| `'hex'`| ` "hex" | "rgb" | "hsl" | "cmyk" | "lab"`Format of the color  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`modelValue`| | ` string`  
`ui`| | ` { root?: ClassNameValue; picker?: ClassNameValue; selector?: ClassNameValue; selectorBackground?: ClassNameValue; selectorThumb?: ClassNameValue; track?: ClassNameValue; trackThumb?: ClassNameValue; }`  
  
### Emits

Event |  Type   
---|---  
`update:modelValue`| `[value: string | undefined]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        colorPicker: {
          slots: {
            root: 'data-[disabled]:opacity-75',
            picker: 'flex gap-4',
            selector: 'rounded-md',
            selectorBackground: 'w-full h-full relative rounded-md',
            selectorThumb: '-translate-y-1/2 -translate-x-1/2 absolute size-4 ring-2 ring-(--color-white) rounded-full cursor-pointer data-[disabled]:cursor-not-allowed',
            track: 'w-[8px] relative rounded-md',
            trackThumb: 'absolute transform -translate-y-1/2 -translate-x-[4px] rtl:translate-x-[4px] size-4 rounded-full ring-2 ring-(--color-white) cursor-pointer data-[disabled]:cursor-not-allowed'
          },
          variants: {
            size: {
              xs: {
                selector: 'w-38 h-38',
                track: 'h-38'
              },
              sm: {
                selector: 'w-40 h-40',
                track: 'h-40'
              },
              md: {
                selector: 'w-42 h-42',
                track: 'h-42'
              },
              lg: {
                selector: 'w-44 h-44',
                track: 'h-44'
              },
              xl: {
                selector: 'w-46 h-46',
                track: 'h-46'
              }
            }
          },
          compoundVariants: [],
          defaultVariants: {
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
            colorPicker: {
              slots: {
                root: 'data-[disabled]:opacity-75',
                picker: 'flex gap-4',
                selector: 'rounded-md',
                selectorBackground: 'w-full h-full relative rounded-md',
                selectorThumb: '-translate-y-1/2 -translate-x-1/2 absolute size-4 ring-2 ring-(--color-white) rounded-full cursor-pointer data-[disabled]:cursor-not-allowed',
                track: 'w-[8px] relative rounded-md',
                trackThumb: 'absolute transform -translate-y-1/2 -translate-x-[4px] rtl:translate-x-[4px] size-4 rounded-full ring-2 ring-(--color-white) cursor-pointer data-[disabled]:cursor-not-allowed'
              },
              variants: {
                size: {
                  xs: {
                    selector: 'w-38 h-38',
                    track: 'h-38'
                  },
                  sm: {
                    selector: 'w-40 h-40',
                    track: 'h-40'
                  },
                  md: {
                    selector: 'w-42 h-42',
                    track: 'h-42'
                  },
                  lg: {
                    selector: 'w-44 h-44',
                    track: 'h-44'
                  },
                  xl: {
                    selector: 'w-46 h-46',
                    track: 'h-46'
                  }
                }
              },
              compoundVariants: [],
              defaultVariants: {
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
            colorPicker: {
              slots: {
                root: 'data-[disabled]:opacity-75',
                picker: 'flex gap-4',
                selector: 'rounded-md',
                selectorBackground: 'w-full h-full relative rounded-md',
                selectorThumb: '-translate-y-1/2 -translate-x-1/2 absolute size-4 ring-2 ring-(--color-white) rounded-full cursor-pointer data-[disabled]:cursor-not-allowed',
                track: 'w-[8px] relative rounded-md',
                trackThumb: 'absolute transform -translate-y-1/2 -translate-x-[4px] rtl:translate-x-[4px] size-4 rounded-full ring-2 ring-(--color-white) cursor-pointer data-[disabled]:cursor-not-allowed'
              },
              variants: {
                size: {
                  xs: {
                    selector: 'w-38 h-38',
                    track: 'h-38'
                  },
                  sm: {
                    selector: 'w-40 h-40',
                    track: 'h-40'
                  },
                  md: {
                    selector: 'w-42 h-42',
                    track: 'h-42'
                  },
                  lg: {
                    selector: 'w-44 h-44',
                    track: 'h-44'
                  },
                  xl: {
                    selector: 'w-46 h-46',
                    track: 'h-46'
                  }
                }
              },
              compoundVariants: [],
              defaultVariants: {
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[CollapsibleA collapsible element to toggle visibility of its
content.](/components/collapsible)[CommandPaletteA command palette with full-
text search powered by Fuse.js for efficient fuzzy
matching.](/components/command-palette)

