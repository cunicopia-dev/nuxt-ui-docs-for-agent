<!-- source: https://ui.nuxt.com/components/page-feature --> # PageFeaturePRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageFeature.vue)

A component to showcase key features of your application.

## Usage

The PageFeature component is used by the [PageSection](/components/page-
section) component to display [features](/components/page-section#features).

### Title

Use the `title` prop to set the title of the feature.

title

Theme

    
    
    <template>
      <UPageFeature title="Theme" />
    </template>
    

### Description

Use the `description` prop to set the description of the feature.

description

Theme

Customize Nuxt UI with your own colors, fonts, and more.

    
    
    <template>
      <UPageFeature
        title="Theme"
        description="Customize Nuxt UI with your own colors, fonts, and more."
      />
    </template>
    

### Icon

Use the `icon` prop to set the icon of the feature.

icon

Theme

Customize Nuxt UI with your own colors, fonts, and more.

    
    
    <template>
      <UPageFeature
        title="Theme"
        description="Customize Nuxt UI with your own colors, fonts, and more."
        icon="i-lucide-swatch-book"
      />
    </template>
    

### Link

You can pass any property from the
[`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link) component such
as `to`, `target`, `rel`, etc.

[](/getting-started/theme)

Theme

Customize Nuxt UI with your own colors, fonts, and more.

    
    
    <template>
      <UPageFeature
        title="Theme"
        description="Customize Nuxt UI with your own colors, fonts, and more."
        icon="i-lucide-swatch-book"
        to="/getting-started/theme"
      />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the feature. Defaults
to `horizontal`.

orientation

vertical

Theme

Customize Nuxt UI with your own colors, fonts, and more.

    
    
    <template>
      <UPageFeature
        orientation="vertical"
        title="Theme"
        description="Customize Nuxt UI with your own colors, fonts, and more."
        icon="i-lucide-swatch-book"
      />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`  
`icon`| | ` string`The icon displayed next to the title when `orientation` is `horizontal` and above the title when `orientation` is `vertical`.  
`target`| | ` null | "_blank" | "_parent" | "_self" | "_top" | string & {}`  
`to`| | ` string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Show properties

  * `name?: RouteRecordNameGeneric`
  * `params?: RouteParamsRawGeneric`
  * `path?: undefined`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>
  * `path: string`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>

  
`title`| | ` string`  
`description`| | ` string`  
`ui`| | ` { root?: ClassNameValue; wrapper?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`title`| `{}`  
`description`| `{}`  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageFeature: {
          slots: {
            root: 'relative',
            wrapper: '',
            leading: 'inline-flex items-center justify-center',
            leadingIcon: 'size-5 shrink-0 text-primary',
            title: 'text-base text-pretty font-semibold text-highlighted',
            description: 'text-[15px] text-pretty text-muted'
          },
          variants: {
            orientation: {
              horizontal: {
                root: 'flex items-start gap-2.5',
                leading: 'p-0.5'
              },
              vertical: {
                leading: 'mb-2.5'
              }
            },
            title: {
              true: {
                description: 'mt-1'
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
            pageFeature: {
              slots: {
                root: 'relative',
                wrapper: '',
                leading: 'inline-flex items-center justify-center',
                leadingIcon: 'size-5 shrink-0 text-primary',
                title: 'text-base text-pretty font-semibold text-highlighted',
                description: 'text-[15px] text-pretty text-muted'
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'flex items-start gap-2.5',
                    leading: 'p-0.5'
                  },
                  vertical: {
                    leading: 'mb-2.5'
                  }
                },
                title: {
                  true: {
                    description: 'mt-1'
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
            pageFeature: {
              slots: {
                root: 'relative',
                wrapper: '',
                leading: 'inline-flex items-center justify-center',
                leadingIcon: 'size-5 shrink-0 text-primary',
                title: 'text-base text-pretty font-semibold text-highlighted',
                description: 'text-[15px] text-pretty text-muted'
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'flex items-start gap-2.5',
                    leading: 'p-0.5'
                  },
                  vertical: {
                    leading: 'mb-2.5'
                  }
                },
                title: {
                  true: {
                    description: 'mt-1'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[PageCTAA call to action section to display in your pages.](/components/page-
cta)[PageGridA responsive grid system for displaying content in a flexible
layout.](/components/page-grid)

