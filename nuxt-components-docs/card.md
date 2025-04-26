<!-- source: https://ui.nuxt.com/components/card --> # Card

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Card.vue)

Display content in a card with a header, body and footer.

## Usage

    
    
    <template>
      <UCard>
        <template #header>
          <Placeholder class="h-8" />
        </template>
    
        <Placeholder class="h-32" />
    
        <template #footer>
          <Placeholder class="h-8" />
        </template>
      </UCard>
    </template>
    

### Variant

Use the `variant` prop to change the variant of the Card.

variant

subtle

    
    
    <template>
      <UCard variant="subtle">
        <template #header>
          <Placeholder class="h-8" />
        </template>
    
        <Placeholder class="h-32" />
    
        <template #footer>
          <Placeholder class="h-8" />
        </template>
      </UCard>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`variant`| `'outline'`| ` "solid" | "outline" | "soft" | "subtle"`  
`ui`| | ` { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`header`| `{}`  
`default`| `{}`  
`footer`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        card: {
          slots: {
            root: 'rounded-lg',
            header: 'p-4 sm:px-6',
            body: 'p-4 sm:p-6',
            footer: 'p-4 sm:px-6'
          },
          variants: {
            variant: {
              solid: {
                root: 'bg-inverted text-inverted'
              },
              outline: {
                root: 'bg-default ring ring-default divide-y divide-default'
              },
              soft: {
                root: 'bg-elevated/50 divide-y divide-default'
              },
              subtle: {
                root: 'bg-elevated/50 ring ring-default divide-y divide-default'
              }
            }
          },
          defaultVariants: {
            variant: 'outline'
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
            card: {
              slots: {
                root: 'rounded-lg',
                header: 'p-4 sm:px-6',
                body: 'p-4 sm:p-6',
                footer: 'p-4 sm:px-6'
              },
              variants: {
                variant: {
                  solid: {
                    root: 'bg-inverted text-inverted'
                  },
                  outline: {
                    root: 'bg-default ring ring-default divide-y divide-default'
                  },
                  soft: {
                    root: 'bg-elevated/50 divide-y divide-default'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default divide-y divide-default'
                  }
                }
              },
              defaultVariants: {
                variant: 'outline'
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
            card: {
              slots: {
                root: 'rounded-lg',
                header: 'p-4 sm:px-6',
                body: 'p-4 sm:p-6',
                footer: 'p-4 sm:px-6'
              },
              variants: {
                variant: {
                  solid: {
                    root: 'bg-inverted text-inverted'
                  },
                  outline: {
                    root: 'bg-default ring ring-default divide-y divide-default'
                  },
                  soft: {
                    root: 'bg-elevated/50 divide-y divide-default'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default divide-y divide-default'
                  }
                }
              },
              defaultVariants: {
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

[CalendarA calendar component for selecting single dates, multiple dates or
date ranges.](/components/calendar)[CarouselA carousel with motion and swipe
built using Embla.](/components/carousel)

