<!-- source: https://ui.nuxt.com/components/footer-columns --> # FooterColumnsPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/FooterColumns.vue)

A list of links as columns to display in your Footer.

## Usage

The FooterColumns component renders a list of columns to display in your
Footer.

Use it in the `top` slot of the [Footer](/components/footer) component:

    
    
    <template>
      <UFooter>
        <template #top>
          <UContainer>
            <UFooterColumns />
          </UContainer>
        </template>
      </UFooter>
    </template>
    

### Columns

Use the `columns` prop as an array of objects with the following properties:

  * `label: string`
  * `children?: { label: string, icon?: string }[]`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

    
    
    <script setup lang="ts">
    import type { FooterColumn } from '@nuxt/ui-pro'
    
    const columns: FooterColumn[] = [
      {
        label: 'Community',
        children: [
          {
            label: 'Nuxters',
            to: 'https://nuxters.nuxt.com',
            target: '_blank'
          },
          {
            label: 'Video Courses',
            to: 'https://masteringnuxt.com/nuxt3?ref=nuxt',
            target: '_blank'
          },
          {
            label: 'Nuxt on GitHub',
            to: 'https://github.com/nuxt',
            target: '_blank'
          }
        ]
      },
      {
        label: 'Solutions',
        children: [
          {
            label: 'Nuxt Content',
            to: 'https://content.nuxt.com/',
            target: '_blank'
          },
          {
            label: 'Nuxt DevTools',
            to: 'https://devtools.nuxt.com/',
            target: '_blank'
          },
          {
            label: 'Nuxt Image',
            to: 'https://image.nuxt.com/',
            target: '_blank'
          },
          {
            label: 'Nuxt UI',
            to: 'https://ui.nuxt.com/',
            target: '_blank'
          }
        ]
      }
    ]
    </script>
    
    <template>
      <UFooterColumns :columns="columns">
        <template #right>
          <UFormField name="email" label="Subscribe to our newsletter" size="lg">
            <UInput type="email" class="w-full">
              <template #trailing>
                <UButton type="submit" size="xs" color="neutral" label="Subscribe" />
              </template>
            </UInput>
          </UFormField>
        </template>
      </UFooterColumns>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'nav'`| `any`The element or component this component should render as.  
`columns`| | ` FooterColumn<FooterColumnLink>[]`  
`ui`| | ` { root?: ClassNameValue; left?: ClassNameValue; center?: ClassNameValue; right?: ClassNameValue; label?: ClassNameValue; ... 5 more ...; linkLabelExternalIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`left`| `{}`  
`default`| `{}`  
`right`| `{}`  
`link`| `{ link: FooterColumnLink; active: boolean; }`  
`link-leading`| `{ link: FooterColumnLink; active: boolean; }`  
`link-label`| `{ link: FooterColumnLink; active: boolean; }`  
`link-trailing`| `{ link: FooterColumnLink; active: boolean; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        footerColumns: {
          slots: {
            root: 'xl:grid xl:grid-cols-3 xl:gap-8',
            left: 'mb-10 xl:mb-0',
            center: 'flex flex-col lg:grid grid-flow-col auto-cols-fr gap-8 xl:col-span-2',
            right: 'mt-10 xl:mt-0',
            label: 'text-sm font-semibold',
            list: 'mt-6 space-y-4',
            item: 'relative',
            link: 'group text-sm flex items-center gap-1.5 focus-visible:outline-primary',
            linkLeadingIcon: 'size-5 shrink-0',
            linkLabel: 'truncate',
            linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed inline-block'
          },
          variants: {
            active: {
              true: {
                link: 'text-primary font-medium'
              },
              false: {
                link: [
                  'text-muted hover:text-default',
                  'transition-colors'
                ]
              }
            }
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
            footerColumns: {
              slots: {
                root: 'xl:grid xl:grid-cols-3 xl:gap-8',
                left: 'mb-10 xl:mb-0',
                center: 'flex flex-col lg:grid grid-flow-col auto-cols-fr gap-8 xl:col-span-2',
                right: 'mt-10 xl:mt-0',
                label: 'text-sm font-semibold',
                list: 'mt-6 space-y-4',
                item: 'relative',
                link: 'group text-sm flex items-center gap-1.5 focus-visible:outline-primary',
                linkLeadingIcon: 'size-5 shrink-0',
                linkLabel: 'truncate',
                linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed inline-block'
              },
              variants: {
                active: {
                  true: {
                    link: 'text-primary font-medium'
                  },
                  false: {
                    link: [
                      'text-muted hover:text-default',
                      'transition-colors'
                    ]
                  }
                }
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
            footerColumns: {
              slots: {
                root: 'xl:grid xl:grid-cols-3 xl:gap-8',
                left: 'mb-10 xl:mb-0',
                center: 'flex flex-col lg:grid grid-flow-col auto-cols-fr gap-8 xl:col-span-2',
                right: 'mt-10 xl:mt-0',
                label: 'text-sm font-semibold',
                list: 'mt-6 space-y-4',
                item: 'relative',
                link: 'group text-sm flex items-center gap-1.5 focus-visible:outline-primary',
                linkLeadingIcon: 'size-5 shrink-0',
                linkLabel: 'truncate',
                linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed inline-block'
              },
              variants: {
                active: {
                  true: {
                    link: 'text-primary font-medium'
                  },
                  false: {
                    link: [
                      'text-muted hover:text-default',
                      'transition-colors'
                    ]
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[FooterA responsive footer component.](/components/footer)[FormA form
component with built-in validation and submission handling.](/components/form)

